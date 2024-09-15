from sqlalchemy import Column, Integer, String, Double
from app.config.db import Base

class Anime(Base):
    __tablename__ = "animes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(500),index=True)
    poster = Column(String(100),index=True)
    rating  = Column((Double))
    episodes = Column(Integer)
    year = Column(Integer)
    genre = Column(String(50))
    status = Column(String(50))
    
