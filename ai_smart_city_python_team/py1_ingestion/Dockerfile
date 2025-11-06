FROM python:3.11-slim
WORKDIR /app
COPY ./app.py /app/app.py
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV API_GATEWAY_URL=${API_GATEWAY_URL:-http://api-gateway:8000}
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
