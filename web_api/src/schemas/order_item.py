from pydantic import BaseModel
from typing import Optional


class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    count: int
    price: float


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemUpdate(BaseModel):
    order_id: Optional[int] = None
    product_id: Optional[int] = None
    count: Optional[int] = None
    price: Optional[float] = None


class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True