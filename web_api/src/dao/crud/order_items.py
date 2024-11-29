from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import OrderItem
from schemas.order_item import OrderItemCreate, OrderItemUpdate


# Получить список продуктов
async def get_order_items(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(OrderItem).offset(skip).limit(limit))
    return result.scalars().all()


# Получить продукт по ID
async def get_order_item(db: AsyncSession, order_item_id: int):
    result = await db.execute(select(OrderItem).where(OrderItem.id == order_item_id))
    return result.scalars().first()


# Создать новый продукт
async def create_order_item(db: AsyncSession, order_item: OrderItemCreate):
    db_order_item = OrderItem(**order_item.dict())
    db.add(db_order_item)
    await db.commit()
    await db.refresh(db_order_item)
    return db_order_item

# Обновить информацию о продукте
async def update_order_item(db: AsyncSession, order_item_id: int, order_item: OrderItemUpdate):
    stmt = (
        update(OrderItem).
        where(OrderItem.id == order_item_id).
        values(**order_item.dict(exclude_unset=True)).
        returning(OrderItem)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить продукт
async def delete_order_item(db: AsyncSession, order_item_id: int):
    stmt = delete(OrderItem).where(OrderItem.id == order_item_id).returning(OrderItem)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
