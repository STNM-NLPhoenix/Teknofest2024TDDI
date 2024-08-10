import json
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import torch

def load_data(filepath):
    # GPU kullanılabilirliği kontrolü
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if device.type == 'cuda':
        print("GPU kullanılacak.")
    else:
        print("GPU kullanılmayacak, CPU kullanılacak.")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def preprocess_data(data):
    texts = []
    entities = []
    sentiments = []

    for item in data:
        text = item['text']
        for entity_info in item['entities']:
            entity = entity_info['entity']
            sentiment = entity_info['sentiment']
            if sentiment == "positive":
                sentiment_label = 2
            elif sentiment == "neutral":
                sentiment_label = 1
            else:
                sentiment_label = 0
            texts.append(text)
            entities.append(entity)
            sentiments.append(sentiment_label)

    df = pd.DataFrame({
        'text': texts,
        'entity': entities,
        'label': sentiments
    })
    return df

def split_data(df):
    X_train, X_test, y_train, y_test = train_test_split(df[['text', 'entity']], df['label'], test_size=0.2, random_state=42)
    train_df = pd.DataFrame({'text': X_train['text'], 'entity': X_train['entity'], 'label': y_train})
    test_df = pd.DataFrame({'text': X_test['text'], 'entity': X_test['entity'], 'label': y_test})
    return train_df, test_df

def create_datasets(train_df, test_df):
    train_dataset = Dataset.from_pandas(train_df)
    test_dataset = Dataset.from_pandas(test_df)
    datasets = DatasetDict({'train': train_dataset, 'test': test_dataset})
    return datasets

def tokenize_function(examples):
    combined_text = [entity + ": " + text for entity, text in zip(examples['entity'], examples['text'])]
    return tokenizer(combined_text, padding="max_length", truncation=True)

def compute_metrics(p):
    preds = p.predictions.argmax(-1)
    precision, recall, f1, _ = precision_recall_fscore_support(p.label_ids, preds, average='weighted')
    acc = accuracy_score(p.label_ids, preds)
    return {
        'accuracy': acc,
        'f1': f1,
        'precision': precision,
        'recall': recall
    }

def predict_sentiment(entity, text):
    combined_text = entity + ": " + text
    inputs = tokenizer(combined_text, return_tensors="pt", padding=True, truncation=True, max_length=128)

    # Move inputs to the same device as the model
    inputs = {k: v.to(model.device) for k, v in inputs.items()}

    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment = torch.argmax(probs).item()
    if sentiment == 2:
        return "positive"
    elif sentiment == 1:
        return "neutral"
    else:
        return "negative"

def main():
    # Veriyi yükle ve işle
    data = load_data("ToplamVeri51K.json")
    df = preprocess_data(data)

    # Veriyi eğitim ve test olarak ayır
    train_df, test_df = split_data(df)

    # Dataset'leri oluştur
    datasets = create_datasets(train_df, test_df)

    # Tokenizer ve model oluştur
    global tokenizer
    tokenizer = BertTokenizer.from_pretrained('dbmdz/bert-base-turkish-cased')
    global model
    model = BertForSequenceClassification.from_pretrained('dbmdz/bert-base-turkish-cased', num_labels=3)

    # Veriyi tokenize et
    tokenized_datasets = datasets.map(tokenize_function, batched=True)
    tokenized_datasets = tokenized_datasets.remove_columns(['text', 'entity'])
    tokenized_datasets = tokenized_datasets.rename_column('label', 'labels')
    tokenized_datasets.set_format('torch')

    # TrainingArguments oluştur
    training_args = TrainingArguments(
        output_dir='./results',
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
    )

    # Trainer oluştur
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets['train'],
        eval_dataset=tokenized_datasets['test'],
        compute_metrics=compute_metrics
    )

    # Modeli eğit
    trainer.train()

    # Modeli değerlendir
    trainer.evaluate()

    # Modeli kaydet
    model.save_pretrained('./absa_model2')
    tokenizer.save_pretrained('./absa_model2')

    # Örnek metin ve varlıklar
    sample_text = "Superonline'ın altyapı yatırımları çok kötü, Turknet'in de müşteri memnuniyeti çok güzel"
    entities = ["Superonline", "Turknet"]

    # Varlık ifadelerini ayır ve duygu tahmini yap
    for entity in entities:
        sentiment = predict_sentiment(entity, sample_text)
        print(f"{entity} hakkında duygu: {sentiment}")

if __name__ == "__main__":
    main()
