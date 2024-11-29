from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Order
from schemas.order import OrderCreate, OrderUpdate


# Получить список продуктов
async def get_orders(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Order).offset(skip).limit(limit))
    return result.scalars().all()


# Получить продукт по ID
async def get_order(db: AsyncSession, order_id: int):
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalars().first()


# Создать новый продукт
async def create_order(db: AsyncSession, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    await db.commit()
    await db.refresh(db_order)
    return db_order

# Обновить информацию о продукте
async def update_order(db: AsyncSession, order_id: int, order: OrderUpdate):
    stmt = (
        update(Order).
        where(Order.id == order_id).
        values(**order.dict(exclude_unset=True)).
        returning(Order)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить продукт
async def delete_order(db: AsyncSession, order_id: int):
    stmt = delete(Order).where(Order.id == order_id).returning(Order)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
