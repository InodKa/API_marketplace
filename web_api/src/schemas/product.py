from pydantic import BaseModel, Field
from typing import Optional


class ProductBase(BaseModel):
    name: str
    category_id: int
    price: float
    description: str


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category_id: Optional[int] = None
    price: Optional[float] = None
    description: Optional[str]


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True