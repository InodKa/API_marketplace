from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Inventory
from schemas.inventory import InventoryCreate, InventoryUpdate


# Получить весь инвентарь
async def get_inventories(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Inventory).offset(skip).limit(limit))
    return result.scalars().all()


# Получить инвентарь по ID
async def get_inventory(db: AsyncSession, inventory_id: int):
    result = await db.execute(select(Inventory).where(Inventory.id == inventory_id))
    return result.scalars().first()


# Создать новый инвентарь
async def create_inventory(db: AsyncSession, inventory: InventoryCreate):
    db_inventory = Inventory(**inventory.dict())
    db.add(db_inventory)
    await db.commit()
    await db.refresh(db_inventory)
    return db_inventory

# Обновить информацию об инвентаре
async def update_inventory(db: AsyncSession, inventory_id: int, inventory: InventoryUpdate):
    stmt = (
        update(Inventory).
        where(Inventory.id == inventory_id).
        values(**inventory.dict(exclude_unset=True)).
        returning(Inventory)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить инвентарь
async def delete_inventory(db: AsyncSession, inventory_id: int):
    stmt = delete(Inventory).where(Inventory.id == inventory_id).returning(Inventory)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()
