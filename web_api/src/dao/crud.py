# src/dao/crud.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from . import models, schemas

class CRUDUser:
    @staticmethod
    async def get_user(db: AsyncSession, user_id: int):
        result = await db.execute(select(models.User).where(models.User.id == user_id))
        return result.scalars().first()
    
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str):
        result = await db.execute(select(models.User).where(models.User.email == email))
        return result.scalars().first()
    
    @staticmethod
    async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
        result = await db.execute(select(models.User).offset(skip).limit(limit))
        return result.scalars().all()
    
    @staticmethod
    async def create_user(db: AsyncSession, user: schemas.UserCreate):
        db_user = models.User(**user.dict())
        db.add(db_user)
        await db.commit()
        await db.refresh(db_user)
        return db_user
    
    @staticmethod
    async def update_user(db: AsyncSession, user_id: int, user: schemas.UserUpdate):
        update_data = user.dict(exclude_unset=True)
        if update_data:
            await db.execute(
                update(models.User).where(models.User.id == user_id).values(**update_data)
            )
            await db.commit()
        return await CRUDUser.get_user(db, user_id)
    
    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int):
        await db.execute(delete(models.User).where(models.User.id == user_id))
        await db.commit()
