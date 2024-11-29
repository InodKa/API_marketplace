from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import transfers
from schemas.transfer import Transfer, TransferCreate, TransferUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/transfers",
    tags=["transfers"],
)

@router.post("/", response_model=Transfer, status_code=201)
async def create_transfer(transfer: TransferCreate, db: AsyncSession = Depends(get_db)):
    db_transfer = await transfers.create_transfer(db, transfer)
    return db_transfer

@router.get("/", response_model=List[Transfer])
async def read_transfers(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    transfer_list = await transfers.get_transfers(db, skip=skip, limit=limit)
    return transfer_list

@router.get("/{transfer_id}", response_model=Transfer)
async def read_transfer(transfer_id: int, db: AsyncSession = Depends(get_db)):
    db_transfer = await transfers.get_transfer(db, transfer_id=transfer_id)
    if db_transfer is None:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return db_transfer

@router.put("/{transfer_id}", response_model=Transfer)
async def update_transfer(transfer_id: int, transfer: TransferUpdate, db: AsyncSession = Depends(get_db)):
    db_transfer = await transfers.update_transfer(db, transfer_id, transfer)
    if db_transfer is None:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return db_transfer

@router.delete("/{transfer_id}", response_model=Transfer)
async def delete_transfer(transfer_id: int, db: AsyncSession = Depends(get_db)):
    db_transfer = await transfers.delete_transfer(db, transfer_id)
    if db_transfer is None:
        raise HTTPException(status_code=404, detail="Transfer not found")
    return db_transfer
