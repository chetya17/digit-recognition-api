from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version

app = FastAPI()

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    feel: int

@app.get("/")
def home():
    return {model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    feel = predict_pipeline(payload.text)
    return {"feel": feel}