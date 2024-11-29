from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from dao.crud import products
from schemas.product import Product, ProductCreate, ProductUpdate
from dao.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.post("/", response_model=Product, status_code=201)
async def create_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    db_product = await products.create_product(db, product)
    return db_product

@router.get("/", response_model=List[Product])
async def read_products(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    product_list = await products.get_products(db, skip=skip, limit=limit)
    return product_list

@router.get("/{product_id}", response_model=Product)
async def read_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await products.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product: ProductUpdate, db: AsyncSession = Depends(get_db)):
    db_product = await products.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/{product_id}", response_model=Product)
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    db_product = await products.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
