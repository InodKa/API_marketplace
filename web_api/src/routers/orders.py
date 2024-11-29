from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import orders
from schemas.order import Order, OrderCreate, OrderUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)

@router.post("/", response_model=Order, status_code=201)
async def create_order(order: OrderCreate, db: AsyncSession = Depends(get_db)):
    db_order = await orders.create_order(db, order)
    return db_order

@router.get("/", response_model=List[Order])
async def read_orders(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    order_list = await orders.get_orders(db, skip=skip, limit=limit)
    return order_list

@router.get("/{order_id}", response_model=Order)
async def read_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await orders.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.put("/{order_id}", response_model=Order)
async def update_order(order_id: int, order: OrderUpdate, db: AsyncSession = Depends(get_db)):
    db_order = await orders.update_order(db, order_id, order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

@router.delete("/{order_id}", response_model=Order)
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await orders.delete_order(db, order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
