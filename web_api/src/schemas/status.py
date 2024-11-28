from pydantic import BaseModel, Field
from typing import Optional


class StatusBase(BaseModel):
    name: str


class StatusCreate(StatusBase):
    pass


class StatusUpdate(BaseModel):
    name: Optional[str] = None


class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True
