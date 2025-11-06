from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
import random

app = FastAPI(title="Model Serving Service - AI Smart City")

@app.get("/health")
async def health_check():
    return {"service": "model_serving", "status": "ok"}

# ✅ FIXED: match your JSON keys exactly
class PredictionRequest(BaseModel):
    sensor_id: str
    features: Dict[str, float]

@app.post("/predict")
async def predict(payload: PredictionRequest):
    score = (
        0.3 * payload.features.get("mean", 0)
        + 0.2 * payload.features.get("max", 0)
        - 0.1 * payload.features.get("min", 0)
        + random.uniform(-0.5, 0.5)
    )
    prediction = "High Congestion" if score > 50 else "Low Congestion"

    return {
        "sensor_id": payload.sensor_id,
        "input_features": payload.features,
        "prediction": prediction,
        "model_score": round(score, 2),
        "status": "Prediction successful"
    }
