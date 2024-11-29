from pydantic import BaseModel
from typing import Optional


class InventoryBase(BaseModel):
    product_id: int
    warehouse_id: int
    count: int


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    product_id: Optional[int] = None
    warehouse_id: Optional[int] = None
    count: Optional[int] = None


class Inventory(InventoryBase):
    id: int

    class Config:
        orm_mode = True