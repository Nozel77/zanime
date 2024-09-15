# app/main.py
from fastapi import FastAPI
from app.routers.auth import auth_router
from app.routers.anime import anime_router 
from app.config.db import init_db

app = FastAPI()

init_db()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(anime_router, prefix="/anime", tags=["anime"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app"}
