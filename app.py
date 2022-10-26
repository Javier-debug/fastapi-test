from fastapi import FastAPI, HTTPException
from uuid import uuid4 as uuid
import uvicorn

app = FastAPI()

@app.get('/')
def read_root():
    return {"welcome": "Welcome to my API"}


    