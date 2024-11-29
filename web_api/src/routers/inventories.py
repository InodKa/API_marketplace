from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import inventories
from schemas.inventory import Inventory, InventoryCreate, InventoryUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/inventories",
    tags=["inventories"],
)

@router.post("/", response_model=Inventory, status_code=201)
async def create_inventory(inventory: InventoryCreate, db: AsyncSession = Depends(get_db)):
    db_inventory = await inventories.create_inventory(db, inventory)
    return db_inventory

@router.get("/", response_model=List[Inventory])
async def read_inventories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    inventory_list = await inventories.get_inventories(db, skip=skip, limit=limit)
    return inventory_list

@router.get("/{inventory_id}", response_model=Inventory)
async def read_inventory(inventory_id: int, db: AsyncSession = Depends(get_db)):
    db_inventory = await inventories.get_inventory(db, inventory_id=inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.put("/{inventory_id}", response_model=Inventory)
async def update_inventory(inventory_id: int, inventory: InventoryUpdate, db: AsyncSession = Depends(get_db)):
    db_inventory = await inventories.update_inventory(db, inventory_id, inventory)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory

@router.delete("/{inventory_id}", response_model=Inventory)
async def delete_inventory(inventory_id: int, db: AsyncSession = Depends(get_db)):
    db_inventory = await inventories.delete_inventory(db, inventory_id)
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return db_inventory
