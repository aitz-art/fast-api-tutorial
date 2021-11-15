from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd
from typing import Optional
app = FastAPI()

class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float  
    
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post('/predict')
async def predict_species(iris: IrisSpecies):
    data = iris.dict()
    loaded_model = pickle.load(open('LRClassifier.pkl', 'rb'))
    data_in = [[data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']]]
    prediction = loaded_model.predict(data_in)
    probability = loaded_model.predict_proba(data_in).max()
    return {
        'prediction': prediction[0],
        'probability': probability
    }