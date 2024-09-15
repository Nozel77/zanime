from fastapi import Depends, HTTPException, status
from app.models.user import User
from app.security.jwt import get_current_user
from sqlalchemy.orm import Session
from app.config.db import SessionLocal
from typing import Generator

def admin_required(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have the necessary permissions"
        )
    return current_user

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()