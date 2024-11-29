from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TransferBase(BaseModel):
    order_id: int
    product_id: int
    from_warehouse_id: int
    to_pickup_point_id: int
    status_id: int
    created_at: datetime
    updated_at: datetime


class TransferCreate(TransferBase):
    pass


class TransferUpdate(BaseModel):
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    from_warehouse_id: Optional[int] = None
    to_pickup_point_id: Optional[int] = None
    status_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Transfer(TransferBase):
    id: int

    class Config:
        orm_mode = True