from pydantic import BaseModel, Field
from typing import Optional


class WarehouseBase(BaseModel):
    address: str
    phone: str = Field(None, pattern=r'^\+7\d{10}$')


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseUpdate(BaseModel):
    address: Optional[str] = None
    phone: Optional[str] = Field(None, pattern=r'^\+7\d{10}$')


class Warehouse(WarehouseBase):
    id: int

    class Config:
        orm_mode = True