from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import pickup_points
from schemas.pickup_point import Pickup_point, Pickup_pointCreate, Pickup_pointUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/pickup_points",
    tags=["pickup_points"],
)

@router.post("/", response_model=Pickup_point, status_code=201)
async def create_pickup_point(pickup_point: Pickup_pointCreate, db: AsyncSession = Depends(get_db)):
    db_pickup_point = await pickup_points.create_pickup_point(db, pickup_point)
    return db_pickup_point

@router.get("/", response_model=List[Pickup_point])
async def read_pickup_points(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    pickup_points_list = await pickup_points.get_pickup_points(db, skip=skip, limit=limit)
    return pickup_points_list

@router.get("/{pickup_point_id}", response_model=Pickup_point)
async def read_pickup_point(pickup_point_id: int, db: AsyncSession = Depends(get_db)):
    db_pickup_point = await pickup_points.get_pickup_point(db, pickup_point_id=pickup_point_id)
    if db_pickup_point is None:
        raise HTTPException(status_code=404, detail="Pickup_point not found")
    return db_pickup_point

@router.put("/{pickup_point_id}", response_model=Pickup_point)
async def update_pickup_point(pickup_point_id: int, pickup_point: Pickup_pointUpdate, db: AsyncSession = Depends(get_db)):
    db_pickup_point = await pickup_points.update_pickup_point(db, pickup_point_id, pickup_point)
    if db_pickup_point is None:
        raise HTTPException(status_code=404, detail="Pickup_point not found")
    return db_pickup_point

@router.delete("/{pickup_point_id}", response_model=Pickup_point)
async def delete_pickup_point(pickup_point_id: int, db: AsyncSession = Depends(get_db)):
    db_pickup_point = await pickup_points.delete_pickup_point(db, pickup_point_id)
    if db_pickup_point is None:
        raise HTTPException(status_code=404, detail="Pickup_point not found")
    return db_pickup_point
