import requests
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

@app.get("/")
def root():
    return {
        "description": "Client Service - orchestrates DB and Business Logic Service calls with token authentication."
    }

@app.get("/health")
def health():
    return {"status": "everything is ok!"}
