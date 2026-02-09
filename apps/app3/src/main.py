from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
def root():
    return {
        "app": "app3",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "app": "app3"
    }

@app.get("/time")
def time():
    return {
        "time": datetime.now(timezone.utc).isoformat(),
        "app": "app3"
    }