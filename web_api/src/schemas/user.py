from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserBase(BaseModel):
    first_name: str = Field(..., max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: str = Field(..., max_length=100)
    email: EmailStr = Field(..., max_length=50)
    phone: Optional[str] = Field(None, regex=r'^\+7\d{10}$')

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=100)
    middle_name: Optional[str] = Field(None, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = Field(None, max_length=50)
    phone: Optional[str] = Field(None, regex=r'^\+7\d{10}$')

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
