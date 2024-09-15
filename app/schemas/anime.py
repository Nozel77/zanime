from pydantic import BaseModel
from typing import List, Optional, Any

class AnimeBase(BaseModel):
    title: str
    description: str
    rating: float
    episodes: int
    year: int
    genre: str
    status: str
    poster: str

    class Config:
        orm_mode = True
        from_attributes = True 

class AnimeCreate(BaseModel):
    title: str
    description: str
    rating: float
    episodes: int
    year: int
    genre: str
    status: str
    poster: str

class AnimeUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    rating: Optional[float] = None
    episodes: Optional[int] = None
    year: Optional[int] = None
    genre: Optional[str] = None
    status: Optional[str] = None
    poster: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True  # Add this line

class AnimeOut(BaseModel):
    id: int
    title: str
    description: str
    rating: float
    episodes: int
    year: int
    genre: str
    status: str
    poster: Optional[str]  

    class Config:
        orm_mode = True
        from_attributes = True

class APIResponse(BaseModel):
    status_code: int
    message: str
    data: Optional[Any] = None

class AnimeListResponse(APIResponse):
    data: List[AnimeOut]
