import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from transformers import BertTokenizerFast, BertForTokenClassification, AdamW, get_linear_schedule_with_warmup
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
from sklearn.metrics import classification_report
import yaml
from itertools import product
from torch.nn import functional as F

"""## Konfigürasyon dosyasını yükleme"""

def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

"""## Veri setini yükleme"""

def load_dataset(file_path):
    df = pd.read_csv(file_path)
    labels = df['label'].unique().tolist()
    label_map = {label: i for i, label in enumerate(labels)}
    reverse_label_map = {i: label for label, i in label_map.items()}
    return df, labels, label_map, reverse_label_map

"""## Dataset sınıfı"""

class NERDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, label_map, max_length):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.label_map = label_map
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx].split()
        label = self.labels[idx].split()
        tokens = self.tokenizer(
            text,
            truncation=True,
            is_split_into_words=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        input_ids = tokens['input_ids'].squeeze(0)
        attention_mask = tokens['attention_mask'].squeeze(0)
        labels = [-100] * len(input_ids)
        word_ids = tokens.word_ids()

        for i, word_id in enumerate(word_ids):
            if word_id is None:
                continue
            if word_id < len(label):
                labels[i] = self.label_map[label[word_id]]

        labels = torch.tensor(labels)
        return {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'labels': labels
        }

"""## Modeli eğitme fonksiyonu"""

def train_model(model, dataloader, optimizer, scheduler, device):
    model.train()
    total_loss = 0

    for batch in tqdm(dataloader, desc="Training"):
        batch_input_ids = batch['input_ids'].to(device)
        batch_attention_mask = batch['attention_mask'].to(device)
        batch_labels = batch['labels'].to(device)

        model.zero_grad()
        outputs = model(
            input_ids=batch_input_ids,
            attention_mask=batch_attention_mask,
            labels=batch_labels
        )

        loss = outputs.loss
        total_loss += loss.item()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()

    avg_train_loss = total_loss / len(dataloader)
    return avg_train_loss

"""## Modeli değerlendirme fonksiyonu"""

def evaluate_model(model, dataloader, device):
    model.eval()
    total_loss = 0
    preds, true_labels = [], []

    for batch in tqdm(dataloader, desc="Evaluating"):
        batch_input_ids = batch['input_ids'].to(device)
        batch_attention_mask = batch['attention_mask'].to(device)
        batch_labels = batch['labels'].to(device)

        with torch.no_grad():
            outputs = model(
                input_ids=batch_input_ids,
                attention_mask=batch_attention_mask,
                labels=batch_labels
            )

        loss = outputs.loss
        total_loss += loss.item()
        logits = outputs.logits.detach().cpu().numpy()
        label_ids = batch_labels.detach().cpu().numpy()

        preds.extend([list(p) for p in np.argmax(logits, axis=2)])
        true_labels.extend(label_ids)

    avg_val_loss = total_loss / len(dataloader)
    return avg_val_loss, preds, true_labels

"""## Ana fonksiyon"""

from sklearn.metrics import accuracy_score

def main(config_path):
    
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print('We will use the GPU:', torch.cuda.get_device_name(0))
        use_cuda = True
    else:
        print('No GPU available, using the CPU instead.')
        device = torch.device("cpu")
        use_cuda = False

    config = load_config(config_path)

    # Konfigürasyonları doğru tiplere dönüştürün
    learning_rate = [float(learning_rate) for learning_rate in config['search']['learning_rates']]  # Float'a çevirin
    batch_size = [int(batch_size) for batch_size in config['search']['batch_sizes']]  # Integer'a çevirin
    epochs = [int(epoch) for epoch in config['search']['epochs']]  # Integer'a çevirin
    adam_epsilon = float(config['training']['adam_epsilon'])  # Float'a çevirin

    print(f"Training with learning_rate={learning_rate}, batch_size={batch_size}, epochs={epochs}")

    df, labels, label_map, reverse_label_map = load_dataset(config['data']['file_path'])

    tokenizer = BertTokenizerFast.from_pretrained(config['model']['name'])
    train_texts, test_texts, train_labels, test_labels = train_test_split(
        df['words'].tolist(), df['label'].tolist(), test_size=config['data']['test_size'], random_state=config['data']['random_state']
    )

    train_dataset = NERDataset(train_texts, train_labels, tokenizer, label_map, config['training']['max_length'])
    test_dataset = NERDataset(test_texts, test_labels, tokenizer, label_map, config['training']['max_length'])

    train_dataloader = DataLoader(train_dataset, batch_size=config['training']['batch_size'], shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=config['training']['batch_size'], shuffle=False)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    best_val_loss = float('inf')
    best_model_state_dict = None
    best_params = None

    param_combinations = list(product(config['search']['learning_rates'], config['search']['batch_sizes'], epochs))

    results = []

    for learning_rate, batch_size, epochs in param_combinations:
        print(f"Training with learning_rate={learning_rate}, batch_size={batch_size}, epochs={epochs}")

        train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

        model = BertForTokenClassification.from_pretrained(config['model']['name'], num_labels=len(labels), ignore_mismatched_sizes=True).to(device)

        optimizer = AdamW(model.parameters(), lr=float(learning_rate), eps=adam_epsilon)
        total_steps = len(train_dataloader) * epochs
        scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=config['training']['warmup_steps'], num_training_steps=total_steps)

        for epoch in range(epochs):
            print(f"Epoch {epoch+1}/{epochs}")
            train_loss = train_model(model, train_dataloader, optimizer, scheduler, device)
            print(f"Training loss: {train_loss}")

            val_loss, preds, true_labels = evaluate_model(model, test_dataloader, device)
            print(f"Validation loss: {val_loss}")

            true_labels_filtered, preds_filtered = [], []
            for true_label, pred in zip(true_labels, preds):
                for tl, p in zip(true_label, pred):
                    if tl != -100:
                        true_labels_filtered.append(tl)
                        preds_filtered.append(p)

            accuracy = accuracy_score(true_labels_filtered, preds_filtered)
            report = classification_report(true_labels_filtered, preds_filtered, target_names=labels, output_dict=True)
            f1_score = report['weighted avg']['f1-score']
            results.append((learning_rate, batch_size, epochs, val_loss, f1_score, accuracy))

            print(f"F1 Score: {f1_score}")
            print(f"Accuracy: {accuracy}")

            if val_loss < best_val_loss:
                best_val_loss = val_loss
                best_model_state_dict = model.state_dict()
                best_params = (learning_rate, batch_size, epochs)

    # En iyi modeli kaydet
    model_save_path = config['model']['save_path']
    torch.save(best_model_state_dict, model_save_path)
    print(f"Best model saved with parameters: learning_rate={best_params[0]}, batch_size={best_params[1]}, epochs={best_params[2]}")

    # Sonuçları bir dosyaya yaz
    with open(config['results']['file_path'], 'w') as file:
        for result in results:
            file.write(f"learning_rate={result[0]}, batch_size={result[1]}, epochs={result[2]}, val_loss={result[3]}, f1_score={result[4]}, accuracy={result[5]}\n")

def test():
    csv_file_path = r'C:\Users\Ertan_N325\Desktop\nlp\STNM_NER\ner_ugur.csv'
    df, labels, label_map, reverse_label_map = load_dataset(csv_file_path)

    # Model ve tokenizer'ı yükleme
    model_load_path = "C:/Users/Ertan_N325/Desktop/nlp/STNM_NER/ugur_saved.pt"  # pt dosyasının yolu
    model = BertForTokenClassification.from_pretrained("akdeniz27/bert-base-turkish-cased-ner", num_labels=len(label_map))
    model.load_state_dict(torch.load(model_load_path))
    model.eval()

    tokenizer = BertTokenizerFast.from_pretrained("akdeniz27/bert-base-turkish-cased-ner")

    # Test verisinin hazırlanması
    test_texts = input("Metin : ")
    test_encodings = tokenizer(test_texts, truncation=True, padding=True, max_length=128, return_tensors="pt")

    # Modelin test edilmesi
    with torch.no_grad():
        outputs = model(**test_encodings)
        predictions = torch.argmax(outputs.logits, dim=2)

    # Sonuçların yorumlanması
    for i, text in enumerate(test_texts):
        input_ids = test_encodings['input_ids'][i]
        tokens = tokenizer.convert_ids_to_tokens(input_ids)
        predicted_labels = [reverse_label_map[label_id.item()] for label_id in predictions[i]]

        # Token'ları ve etiketleri birleştirerek tam kelimeler oluşturma
        word_tokens = []
        word_labels = []
        current_word = ""
        current_label = None

        for token, label in zip(tokens, predicted_labels):
            if token.startswith("##"):
                current_word += token[2:]
            else:
                if current_word:
                    word_tokens.append(current_word)
                    word_labels.append(current_label)
                current_word = token
                current_label = label

        if current_word:
            word_tokens.append(current_word)
            word_labels.append(current_label)

        print(f"\nText: {text}")
        for word, label in zip(word_tokens, word_labels):
            print(f"{word}: {label}")


if __name__ == "__main__":
    main("ugur_config2.yaml")
    i = 0
    while(i<10):
        test()
        i+=1