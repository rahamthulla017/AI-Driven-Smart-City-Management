from fastapi import FastAPI, Request, Body
import httpx, asyncio

app = FastAPI(title="AI Smart City - Main API Gateway")

# Local services running on different ports
SERVICE_MAP = {
    "ingestion": "http://localhost:8001",
    "feature": "http://localhost:8002",
    "model": "http://localhost:8003",
    "automation": "http://localhost:8004",
}


# ----------------- ROOT & HEALTH -----------------
@app.get("/")
async def home():
    return {
        "message": "🚀 AI Smart City Gateway is running",
        "services": list(SERVICE_MAP.keys()),
        "routes": {
            "ingest": "/ingest",
            "features": "/features",
            "predict": "/predict",
            "trigger": "/trigger"
        }
    }


@app.get("/health")
async def health():
    """Ping all 4 services to verify they are alive"""
    results = {}
    async with httpx.AsyncClient() as client:
        for key, base in SERVICE_MAP.items():
            try:
                res = await client.get(f"{base}/health")
                results[key] = res.json()
            except Exception as e:
                results[key] = {"status": "error", "detail": str(e)}
    return results


# ----------------- PROXY ROUTES -----------------
@app.post("/ingest")
async def forward_ingest(data: dict = Body(...)):
    """Forward request to Ingestion service"""
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{SERVICE_MAP['ingestion']}/ingest", json=data)
        return res.json()


@app.post("/features")
async def forward_features(data: dict = Body(...)):
    """Forward request to Feature Engineering service"""
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{SERVICE_MAP['feature']}/features", json=data)
        return res.json()


@app.post("/predict")
async def forward_predict(data: dict = Body(...)):
    """Forward request to Model Serving service"""
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{SERVICE_MAP['model']}/predict", json=data)
        return res.json()


@app.post("/trigger")
async def forward_trigger(data: dict = Body(...)):
    """Forward request to Automation service"""
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{SERVICE_MAP['automation']}/trigger", json=data)
        return res.json()
