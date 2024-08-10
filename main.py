from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from transformers import BertTokenizer, BertForTokenClassification, BertForSequenceClassification
from starlette.requests import Request
from fastapi.staticfiles import StaticFiles
import torch
import requests

# NER modeli ve tokenizer
ner_model_name = r"C:\Users\talha\Desktop\Teknofest-GUI\NER_Modeli"
ner_model = BertForTokenClassification.from_pretrained(ner_model_name, num_labels=7, ignore_mismatched_sizes=True)
ner_tokenizer = BertTokenizer.from_pretrained(ner_model_name)

# ABSA modeli ve tokenizer
absa_model_name = r'C:\Users\talha\Desktop\Teknofest-GUI\absa_model3'
absa_model = BertForSequenceClassification.from_pretrained(absa_model_name, num_labels=3)
absa_tokenizer = BertTokenizer.from_pretrained(absa_model_name)

# Duygu durumlarını anlamlı etiketlere dönüştüren bir sözlük
sentiment_labels = {
    0: 'olumsuz',
    1: 'nötr',
    2: 'olumlu'
}

# FastAPI uygulamasını oluştur
app = FastAPI()

# Şablonlar
templates = Jinja2Templates(directory="templates")

# Statik dosyaları servis etmek için
app.mount("/static", StaticFiles(directory="static"), name="static")

# Ana sayfa
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# NER tahmin fonksiyonu
def ner_predict(text):
    inputs = ner_tokenizer(text, return_tensors="pt").to(ner_model.device)
    with torch.no_grad():
        outputs = ner_model(**inputs)
        logits = outputs.logits
    predictions = torch.argmax(logits, dim=2)
    tokens = ner_tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    labels = predictions[0].cpu().numpy()

    label_map = {
        0: "B-LOC",
        1: "B-ORG",
        2: "B-PER",
        3: "I-LOC",
        4: "I-ORG",
        5: "I-PER",
        6: "O"
    }

    org_entities = []
    current_entity = []

    for token, label in zip(tokens, labels):
        if token in ["[CLS]", "[SEP]"]:
            continue  # [CLS] ve [SEP] tokenlerini atla
        if label_map[label] == "B-ORG":
            if current_entity:
                org_entities.append(current_entity)
                current_entity = []
            current_entity.append(token)
        elif label_map[label] == "I-ORG" and current_entity:
            current_entity.append(token)
        else:
            if current_entity:
                org_entities.append(current_entity)
                current_entity = []

    if current_entity:
        org_entities.append(current_entity)

    entities = [ner_tokenizer.convert_tokens_to_string(entity) for entity in org_entities]
    return entities

# ABSA duygu tahmin fonksiyonu
def predict_sentiment(entity, text):
    combined_text = entity + ": " + text
    inputs = absa_tokenizer(combined_text, return_tensors="pt", padding=True, truncation=True, max_length=256)
    inputs = {k: v.to(absa_model.device) for k, v in inputs.items()}
    outputs = absa_model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment = torch.argmax(probs).item()
    return sentiment_labels.get(sentiment, 'Bilinmiyor')

# Tahmin endpoint'i
@app.post("/predict/", response_class=JSONResponse)
def predict(request: Request, payload: dict):
    text = payload.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="Text field is required")

    # Ön işleme microservice'ini çağırma
    preprocess_response = requests.post("http://localhost:6006/preprocess/", json={"text": text})
    if preprocess_response.status_code == 200:
        processed_text = preprocess_response.json()["processed_text"]
    else:
        raise HTTPException(status_code=500, detail="Preprocessing microservice error")

    # NER tahmini
    entities = ner_predict(processed_text)

    # ABSA tahmini için tespit edilen varlıklar üzerinde döngü
    results = []
    for entity in entities:
        sentiment = predict_sentiment(entity, processed_text)
        results.append({
            'entity': entity,
            'sentiment': sentiment
        })

    # Nihai JSON çıktısı
    final_output = {
        "entity_list": entities,
        "results": results
    }

    # JSON yanıtını döndür
    return JSONResponse(content=final_output)