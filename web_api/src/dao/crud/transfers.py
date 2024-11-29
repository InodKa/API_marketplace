from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Transfer
from schemas.transfer import TransferCreate, TransferUpdate


# Получить список продуктов
async def get_transfers(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Transfer).offset(skip).limit(limit))
    return result.scalars().all()


# Получить продукт по ID
async def get_transfer(db: AsyncSession, transfer_id: int):
    result = await db.execute(select(Transfer).where(Transfer.id == transfer_id))
    return result.scalars().first()


# Создать новый продукт
async def create_transfer(db: AsyncSession, transfer: TransferCreate):
    db_transfer = Transfer(**transfer.dict())
    db.add(db_transfer)
    await db.commit()
    await db.refresh(db_transfer)
    return db_transfer

# Обновить информацию о продукте
async def update_transfer(db: AsyncSession, transfer_id: int, transfer: TransferUpdate):
    stmt = (
        update(Transfer).
        where(Transfer.id == transfer_id).
        values(**transfer.dict(exclude_unset=True)).
        returning(Transfer)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить продукт
async def delete_transfer(db: AsyncSession, transfer_id: int):
    stmt = delete(Transfer).where(Transfer.id == transfer_id).returning(Transfer)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
