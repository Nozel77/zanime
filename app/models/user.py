from sqlalchemy import Column, Integer, String
from app.config.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    role = Column(String(50), default="user")
    
