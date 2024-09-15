# test_main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_root():
    return {"message": "Hello World"}
