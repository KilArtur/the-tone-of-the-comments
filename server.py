import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
base_model_pipeline = joblib.load("./base_model_pipeline.joblib")

class ToxicComments(BaseModel):
    type: str

@app.post('/predict')
def predict(text: ToxicComments):
    """
    Предсказание токсичности комментариев
    """
    comment = text.type
    prediction = base_model_pipeline.predict([comment]).tolist()[0]
    return {"toxic": prediction}

