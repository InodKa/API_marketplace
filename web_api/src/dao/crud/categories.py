from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Category
from schemas.category import CategoryCreate, CategoryUpdate


# Получить список категорий
async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Category).offset(skip).limit(limit))
    return result.scalars().all()


# Получить категорию по ID
async def get_category(db: AsyncSession, category_id: int):
    result = await db.execute(select(Category).where(Category.id == category_id))
    return result.scalars().first()


# Создать новую категорию
async def create_category(db: AsyncSession, category: CategoryCreate):
    db_category = Category(**category.dict())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)
    return db_category

# Обновить информацию о категории
async def update_category(db: AsyncSession, category_id: int, category: CategoryUpdate):
    stmt = (
        update(Category).
        where(Category.id == category_id).
        values(**category.dict(exclude_unset=True)).
        returning(Category)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить категорию
async def delete_category(db: AsyncSession, category_id: int):
    stmt = delete(Category).where(Category.id == category_id).returning(Category)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
