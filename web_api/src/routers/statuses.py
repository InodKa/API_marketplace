from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from web_api.src.dao.crud import users
from schemas.status import Status, StatusCreate, StatusUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/statuses",
    tags=["statuses"],
)

@router.post("/", response_model=Status, status_code=201)
async def create_status(Status: StatusCreate, db: AsyncSession = Depends(get_db)):
    db_status = await users.create_status(db, Status)
    return db_status

@router.get("/", response_model=List[Status])
async def read_statuses(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    statuses = await users.get_statuses(db, skip=skip, limit=limit)
    return statuses

@router.get("/{status_id}", response_model=Status)
async def read_Status(status_id: int, db: AsyncSession = Depends(get_db)):
    db_status = await users.get_status(db, status_id=status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status

@router.put("/{status_id}", response_model=Status)
async def update_Status(status_id: int, Status: StatusUpdate, db: AsyncSession = Depends(get_db)):
    db_status = await users.update_Status(db, status_id, Status)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status

@router.delete("/{status_id}", response_model=Status)
async def delete_Status(status_id: int, db: AsyncSession = Depends(get_db)):
    db_status = await users.delete_Status(db, status_id)
    if db_status is None:
        raise HTTPException(status_code=404, detail="Status not found")
    return db_status
