from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, LoginResponse, UserRegisterResponse, LoginData
from app.models.user import User
from app.config.db import SessionLocal
from passlib.context import CryptContext
from app.security.jwt import create_access_token, verify_token


auth_router = APIRouter()

# Hashing password setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBasic()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_password(plain_password: str, password: str) -> bool:
    return pwd_context.verify(plain_password, password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

@auth_router.post("/register", response_model=UserRegisterResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user_by_email = db.query(User).filter(User.email == user.email).first()
    if db_user_by_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {
        "status_code": 201,
        "message": "User successfully created",
        "data": UserOut.from_orm(new_user)
    }

@auth_router.post("/login", response_model=LoginResponse)
def login(credentials: HTTPBasicCredentials, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == credentials.username).first()
    if db_user and verify_password(credentials.password, db_user.password):
        access_token = create_access_token(data={"sub": db_user.username})
        login_data = LoginData(username=db_user.username, access_token=access_token)
        return {
            "status_code": 200,
            "message": "Login successful",
            "data": login_data
        }
    raise HTTPException(status_code=401, detail="Invalid credentials")


@auth_router.post("/logout")
def logout(response: Response):
    response.delete_cookie("user_id")
    return {"status_code": 200, "message": "Logout successful"}
