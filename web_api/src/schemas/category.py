from pydantic import BaseModel, Field
from typing import Optional


class CategoryBase(BaseModel):
    parent_id: Optional[int] = None
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    parent_id: Optional[int] = None
    name: Optional[str] = None


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True