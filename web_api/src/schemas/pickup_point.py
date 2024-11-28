from pydantic import BaseModel, Field
from typing import Optional


class Pickup_pointBase(BaseModel):
    address: str
    phone: str = Field(None, pattern=r'^\+7\d{10}$')


class Pickup_pointCreate(Pickup_pointBase):
    pass


class Pickup_pointUpdate(BaseModel):
    address: Optional[str] = None
    phone: Optional[str] = Field(None, pattern=r'^\+7\d{10}$')


class Pickup_point(Pickup_pointBase):
    id: int

    class Config:
        orm_mode = True
        

