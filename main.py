from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version
import json
from types import SimpleNamespace

app = FastAPI()

path = '1.png'

class PredictionOut(BaseModel):
    text: list


@app.get("/")
def home():
    return {model_version}


@app.post("/predict", response_model=PredictionOut)
def predict(path: str):
    text = predict_pipeline(path)
    return {"text": text}

# payload: TextIn
# /{path}