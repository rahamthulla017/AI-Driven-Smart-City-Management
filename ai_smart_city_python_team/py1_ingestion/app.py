from fastapi import FastAPI
import os
app = FastAPI(title="PY1 - Ingestion")

@app.get("/health")
def health():
    return {"service": "ingestion", "status": "ok"}

@app.post("/ingest")
async def ingest(payload: dict):
    # placeholder: validate & store to S3/RDS/Kinesis
    return {"received": True, "size": len(payload)}
