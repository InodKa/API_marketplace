from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Product
from schemas.product import ProductCreate, ProductUpdate


# Получить список продуктов
async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    return result.scalars().all()


# Получить продукт по ID
async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalars().first()


# Создать новый продукт
async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product

# Обновить информацию о продукте
async def update_product(db: AsyncSession, product_id: int, product: ProductUpdate):
    stmt = (
        update(Product).
        where(Product.id == product_id).
        values(**product.dict(exclude_unset=True)).
        returning(Product)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить продукт
async def delete_product(db: AsyncSession, product_id: int):
    stmt = delete(Product).where(Product.id == product_id).returning(Product)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
