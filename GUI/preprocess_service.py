from fastapi import FastAPI
from pydantic import BaseModel
import re

app = FastAPI()

class TextData(BaseModel):
    text: str

# Ön işleme fonksiyonları
def keep_punctuation(text: str) -> str:
    # Nokta ve virgül haricindeki tüm noktalama işaretlerini boşlukla değiştir
    return re.sub(r'[^\w\s.,]', ' ', text)

def keep_stop_words(text: str) -> str:
    return text

def no_stemming_lemmatization(text: str) -> str:
    return text

def clean_repeated_spaces_chars(text: str) -> str:
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def custom_case_conversion(text: str) -> str:
    words = text.split()
    for i, word in enumerate(words):
        if word.isupper():
            continue
        else:
            words[i] = word.lower()
    return ' '.join(words)

def remove_special_symbols(text: str) -> str:
    # @ ve # işaretlerini kaldır
    return re.sub(r'[@#]', '', text)

@app.get("/")
def read_root():
    return {"message": "Preprocess service is running"}

@app.post("/preprocess/")
def preprocess(data: TextData):
    text = data.text

    text = keep_punctuation(text)  # Noktalama işaretlerini işleme
    text = keep_stop_words(text)
    text = no_stemming_lemmatization(text)
    text = remove_special_symbols(text)
    text = clean_repeated_spaces_chars(text)
    text = custom_case_conversion(text)

    return {"processed_text": text}