from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import warehouses
from schemas.warehouse import Warehouse, WarehouseCreate, WarehouseUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/warehouses",
    tags=["warehouses"],
)

@router.post("/", response_model=Warehouse, status_code=201)
async def create_warehouse(warehouse: WarehouseCreate, db: AsyncSession = Depends(get_db)):
    db_warehouse = await warehouses.create_warehouse(db, warehouse)
    return db_warehouse

@router.get("/", response_model=List[Warehouse])
async def read_warehouses(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    warehouses_list = await warehouses.get_warehouses(db, skip=skip, limit=limit)
    return warehouses_list

@router.get("/{warehouse_id}", response_model=Warehouse)
async def read_warehouse(warehouse_id: int, db: AsyncSession = Depends(get_db)):
    db_warehouse = await warehouses.get_warehouse(db, warehouse_id=warehouse_id)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@router.put("/{warehouse_id}", response_model=Warehouse)
async def update_warehouse(warehouse_id: int, warehouse: WarehouseUpdate, db: AsyncSession = Depends(get_db)):
    db_warehouse = await warehouses.update_warehouse(db, warehouse_id, warehouse)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse

@router.delete("/{warehouse_id}", response_model=Warehouse)
async def delete_warehouse(warehouse_id: int, db: AsyncSession = Depends(get_db)):
    db_warehouse = await warehouses.delete_warehouse(db, warehouse_id)
    if db_warehouse is None:
        raise HTTPException(status_code=404, detail="Warehouse not found")
    return db_warehouse
