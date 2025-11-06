🧠 AI-Driven Smart City Management System — Python Team
🚀 Overview

This repository contains the Python backend microservices and API Gateway for the AI-Driven Smart City Management System.
The Python team’s modules are responsible for data ingestion, feature engineering, model serving, and automation workflows.

All services are built using FastAPI and communicate through a unified Main API Gateway.

🏗️ Python Microservice Architecture
Service	Port	Description
PY1 - Ingestion	8001	Receives raw IoT/sensor data (JSON, CSV, streams) and pushes it to storage or message queues (e.g., S3, RDS, or Kinesis).
PY2 - Feature Engineering	8002	Performs feature extraction, sliding window aggregation, anomaly scoring, and feature caching.
PY3 - Model Serving	8003	Hosts AI/ML models (e.g., traffic prediction, anomaly detection) and serves predictions via REST API.
PY4 - Automation & DataOps	8004	Triggers retraining, monitors data drift, and manages automated workflows.
Main API Gateway	8000	Routes all requests to the appropriate service through a single unified endpoint.
🧩 Folder Structure
ai_smart_city_python_team/
│
├── main_api_gateway/
│   └── main_api_gateway.py      # Central router for all Python microservices
│
├── py1_ingestion/
│   └── app.py                   # Ingestion Service
│
├── py2_feature_engineer/
│   └── app.py                   # Feature Engineering Service
│
├── py3_model_serving/
│   └── app.py                   # Model Serving Service
│
├── py4_automation/
│   └── app.py                   # Automation / DataOps Service
│
├── requirements.txt             # Python dependencies
└── README.md                    # This documentation


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-repo>/ai_smart_city_python_team.git
cd ai_smart_city_python_team

2️⃣ Create a Virtual Environment
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run All Microservices (in separate terminals)
Service	Command	URL
PY1	uvicorn py1_ingestion.app:app --reload --port 8001	http://localhost:8001/docs

PY2	uvicorn py2_feature_engineer.app:app --reload --port 8002	http://localhost:8002/docs

PY3	uvicorn py3_model_serving.app:app --reload --port 8003	http://localhost:8003/docs

PY4	uvicorn py4_automation.app:app --reload --port 8004	http://localhost:8004/docs

Gateway	uvicorn main_api_gateway.main_api_gateway:app --reload --port 8000	http://localhost:8000/docs
🌐 Unified API Gateway

Once all services are running, the gateway (port 8000) provides one endpoint for the entire Python backend.

Base URL
http://localhost:8000

Available Endpoints
Endpoint	Method	Description	Forwards To
/ingest	POST	Ingest IoT data	PY1 - Ingestion
/features	POST	Extract features	PY2 - Feature Engineering
/predict	POST	Get model predictions	PY3 - Model Serving
/trigger	POST	Trigger automation/retraining	PY4 - Automation
/health	GET	Check all service health	All microservices
📦 Example Requests
🔹 Ingest Data
POST http://localhost:8000/ingest
Content-Type: application/json

{
  "sensor_id": "traffic_sensor_42",
  "timestamp": "2025-11-06T10:00:00Z",
  "traffic_count": 150,
  "air_quality_index": 85
}

🔹 Extract Features
POST http://localhost:8000/features
Content-Type: application/json

{
  "sensor_id": "traffic_sensor_42",
  "data_points": [45, 50, 55, 60, 65]
}

🔹 Get Model Prediction
POST http://localhost:8000/predict
Content-Type: application/json

{
  "data": {
    "sensor_id": "traffic_sensor_42",
    "features": {
      "mean": 55,
      "max": 65,
      "min": 45
    }
  }
}

🔹 Trigger Automation
POST http://localhost:8000/trigger
Content-Type: application/json

{
  "task": "retrain_model",
  "dataset": "traffic_data_v2",
  "triggered_by": "schedule"
}

🧪 Health Check

Check if all services are alive:

GET http://localhost:8000/health


Response example:

{
  "ingestion": {"service": "ingestion", "status": "ok"},
  "feature": {"service": "feature", "status": "ok"},
  "model": {"service": "model", "status": "ok"},
  "automation": {"service": "automation", "status": "ok"}
}

🐳 Docker (Optional)

Each service includes a Dockerfile for containerized deployment.
To build and run all containers:

docker compose up --build

👥 Team Responsibilities
Member	Role	Focus
PY1	Data Engineer	Ingestion, data validation, ETL pipelines
PY2	ML Engineer	Feature engineering, data transformation
PY3	AI/ML Developer	Model serving, prediction API
PY4	Automation Engineer	Cron jobs, data drift detection, triggers
🏁 Summary

✅ 4 Python FastAPI microservices
✅ Unified API Gateway (Port 8000)
✅ Swagger UI for all endpoints
✅ Modular, container-ready structure
✅ Ready for integration with Java, React, and AWS infrastructure
