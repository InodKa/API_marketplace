from pydantic import BaseModel, Field
from typing import Optional


class StatusBase(BaseModel):
    name: str


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True
