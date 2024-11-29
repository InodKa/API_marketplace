from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OrderBase(BaseModel):
    user_id: int
    pickup_point_id: int
    total_cost: float
    status_id: int
    created_at: datetime
    updated_at: datetime


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    pickup_point_id: Optional[int] = None
    total_cost: Optional[float] = None
    status_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True