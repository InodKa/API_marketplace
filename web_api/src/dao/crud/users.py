from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import User
from schemas.user import UserCreate, UserUpdate


# Получить список пользователей с пагинацией
async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


# Получить пользователя по ID
async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


# Создать нового пользователя
async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

# Обновить информацию о пользователе
async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
    stmt = (
        update(User).
        where(User.id == user_id).
        values(**user.dict(exclude_unset=True)).
        returning(User)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить пользователя
async def delete_user(db: AsyncSession, user_id: int):
    stmt = delete(User).where(User.id == user_id).returning(User)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
