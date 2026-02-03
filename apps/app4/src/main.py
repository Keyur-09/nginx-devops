from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get("/health")
def health():
    return{"status": "ok","app":"app4"}

@app.get("/time")
def time():
    return{
        "time": datetime.now(timezone.utc).isoformat()
    }