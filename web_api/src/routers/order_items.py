from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import order_items
from schemas.order_item import OrderItem, OrderItemCreate, OrderItemUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/order_items",
    tags=["order_items"],
)

@router.post("/", response_model=OrderItem, status_code=201)
async def create_order_item(order_item: OrderItemCreate, db: AsyncSession = Depends(get_db)):
    db_order_item = await order_items.create_order_item(db, order_item)
    return db_order_item

@router.get("/", response_model=List[OrderItem])
async def read_order_items(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    order_item_list = await order_items.get_order_items(db, skip=skip, limit=limit)
    return order_item_list

@router.get("/{order_item_id}", response_model=OrderItem)
async def read_order_item(order_item_id: int, db: AsyncSession = Depends(get_db)):
    db_order_item = await order_items.get_order_item(db, order_item_id=order_item_id)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")
    return db_order_item

@router.put("/{order_item_id}", response_model=OrderItem)
async def update_order_item(order_item_id: int, order_item: OrderItemUpdate, db: AsyncSession = Depends(get_db)):
    db_order_item = await order_items.update_order_item(db, order_item_id, order_item)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")
    return db_order_item

@router.delete("/{order_item_id}", response_model=OrderItem)
async def delete_order_item(order_item_id: int, db: AsyncSession = Depends(get_db)):
    db_order_item = await order_items.delete_order_item(db, order_item_id)
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="OrderItem not found")
    return db_order_item
