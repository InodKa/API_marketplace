from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Pickup_point
from schemas.pickup_point import Pickup_pointCreate, Pickup_pointUpdate



# Получить ПВЗ
async def get_pickup_points(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Pickup_point).offset(skip).limit(limit))
    return result.scalars().all()


# Получить ПВЗ по ID
async def get_pickup_point(db: AsyncSession, pickup_point_id: int):
    result = await db.execute(select(Pickup_point).where(Pickup_point.id == pickup_point_id))
    return result.scalars().first()


# Создать новый ПВЗ
async def create_pickup_point(db: AsyncSession, pickup_point: Pickup_pointCreate):
    db_pickup_point = Pickup_point(**pickup_point.dict())
    db.add(db_pickup_point)
    await db.commit()
    await db.refresh(db_pickup_point)
    return db_pickup_point


# Обновить информацию о ПВЗ
async def update_pickup_point(db: AsyncSession,  pickup_point_id: int,  pickup_point:  Pickup_pointUpdate):
    stmt = (
        update( Pickup_point).
        where( Pickup_point.id ==  pickup_point_id).
        values(** pickup_point.dict(exclude_unset=True)).
        returning( Pickup_point)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить ПВЗ
async def delete_pickup_point(db: AsyncSession,  pickup_point_id: int):
    stmt = delete( Pickup_point).where( Pickup_point.id ==  pickup_point_id).returning( Pickup_point)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()

