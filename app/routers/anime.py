from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.anime import AnimeCreate, AnimeUpdate, AnimeOut, AnimeListResponse, APIResponse
from app.models.anime import Anime
from app.config.db import SessionLocal
from typing import List
from app.security.dependencies import admin_required

anime_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@anime_router.get("", response_model=AnimeListResponse)
def list_animes(db: Session = Depends(get_db)):
    db_animes = db.query(Anime).all()
    return {
        "status_code": 200,
        "message": "Data berhasil diambil",
        "data": [AnimeOut.from_orm(anime) for anime in db_animes]
    }


@anime_router.get("/{anime_id}", response_model=APIResponse)
def read_anime(anime_id: int, db: Session = Depends(get_db)):
    db_anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    return {
        "status_code": 200,
        "message": "Data berhasil diambil",
        "data": AnimeOut.from_orm(db_anime)
    }

@anime_router.post("/store", response_model=APIResponse, dependencies=[Depends(admin_required)])
def create_anime(anime: AnimeCreate, db: Session = Depends(get_db)):
    db_anime = Anime(
        title=anime.title,
        description=anime.description,
        rating=anime.rating,
        episodes=anime.episodes,
        year=anime.year,
        genre=anime.genre,
        status=anime.status,
        poster=anime.poster
    )
    db.add(db_anime)
    db.commit()
    db.refresh(db_anime)
    return {
        "status_code": 201,
        "message": "Data berhasil dibuat",
        "data": AnimeOut.from_orm(db_anime)
    }


@anime_router.put("/update/{anime_id}", response_model=APIResponse, dependencies=[Depends(admin_required)])
def update_anime(anime_id: int, anime: AnimeUpdate, db: Session = Depends(get_db)):
    db_anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    for key, value in anime.dict(exclude_unset=True).items():
        setattr(db_anime, key, value)
    
    db.commit()
    db.refresh(db_anime)
    return {
        "status_code": 200,
        "message": "Data berhasil diperbarui",
        "data": AnimeOut.from_orm(db_anime)
    }


@anime_router.delete("/delete/{anime_id}", response_model=APIResponse, dependencies=[Depends(admin_required)])
def delete_anime(anime_id: int, db: Session = Depends(get_db)):
    db_anime = db.query(Anime).filter(Anime.id == anime_id).first()
    if db_anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    
    db.delete(db_anime)
    db.commit()
    return {
        "status_code": 200,
        "message": "Data berhasil dihapus",
        "data": AnimeOut.from_orm(db_anime)
    }

