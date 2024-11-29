from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import categories
from schemas.category import Category, CategoryCreate, CategoryUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)

@router.post("/", response_model=Category, status_code=201)
async def create_category(category: CategoryCreate, db: AsyncSession = Depends(get_db)):
    db_category = await categories.create_category(db, category)
    return db_category

@router.get("/", response_model=List[Category])
async def read_categories(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    category_list = await categories.get_categories(db, skip=skip, limit=limit)
    return category_list

@router.get("/{category_id}", response_model=Category)
async def read_category(category_id: int, db: AsyncSession = Depends(get_db)):
    db_category = await categories.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.put("/{category_id}", response_model=Category)
async def update_category(category_id: int, category: CategoryUpdate, db: AsyncSession = Depends(get_db)):
    db_category = await categories.update_category(db, category_id, category)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

@router.delete("/{category_id}", response_model=Category)
async def delete_category(category_id: int, db: AsyncSession = Depends(get_db)):
    db_category = await categories.delete_category(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category
