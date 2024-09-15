# app/schemas/user.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: str = "user"  

    class Config:
        schema_extra = {
            "example": {
                "username": "john_doe",
                "email": "john.doe@example.com",
                "password": "securepassword",
                "role": "user"
            }
        }

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True
        from_attributes=True

class UserRegisterResponse(BaseModel):
    status_code: int
    message: str
    data: UserOut

    class Config:
        from_attributes=True

class LoginData(BaseModel):
    username: str
    access_token: str

class LoginResponse(BaseModel):
    status_code: int
    message: str
    data: LoginData  

    class Config:
        orm_mode = True

class TokenData(BaseModel):
    username: str
    role: str

    class Config:
        orm_mode = True