from fastapi import FastAPI
from pydantic import BaseModel
from model.model import predict_pipeline
from model.model import __version__ as model_version
import json
from types import SimpleNamespace

app = FastAPI()

class TextIn(BaseModel):
    text: str
    # x = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))


class PredictionOut(BaseModel):
    feel: int

@app.get("/")
def home():
    return {model_version}

@app.post("/predict/{text}", response_model=PredictionOut)
def predict(text: str):
    feel = predict_pipeline(text)
    return {"feel": feel}

# payload: TextIn