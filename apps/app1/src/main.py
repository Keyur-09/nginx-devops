from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/health")
def health():
    return{"status": "ok"}

@app.get("/time")
def time():
    return{
        "time": datetime.now(timezone.utc).isoformat()
    }
@app.get("/")
def root():
    return {"app": "app1", "status": "running"}