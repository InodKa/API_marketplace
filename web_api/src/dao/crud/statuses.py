from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Status
from schemas.status import StatusCreate


# Получить список статусов 
async def get_statuses(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Status).offset(skip).limit(limit))
    return result.scalars().all()


# Получиить статус по id
async def get_status(db: AsyncSession, status_id: int):
    result = await db.execute(select(Status).where(Status.id == status_id))
    return result.scalars().first()


# Создать новый статус
async def create_status(db: AsyncSession, status: StatusCreate):
    db_status = Status(**status.dict())
    db.add(db_status)
    await db.commit()
    await db.refresh(db_status)
    return db_status


# Удалить статус
async def delete_status(db: AsyncSession, status_id: int):
    result = await db.execute(delete(Status).where(Status.id == status_id).returning(Status))
    await db.commit()
    return result.scalars().first()