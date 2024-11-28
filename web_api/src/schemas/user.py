from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: EmailStr
    phone: str = Field(None, pattern=r'^\+7\d{10}$')

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, pattern=r'^\+7\d{10}$')

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
