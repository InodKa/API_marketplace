from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from ..models import Warehouse
from schemas.warehouse import WarehouseCreate, WarehouseUpdate



# Получить все склады
async def get_warehouses(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Warehouse).offset(skip).limit(limit))
    return result.scalars().all()


# Получить склад по ID
async def get_warehouse(db: AsyncSession, warehouse_id: int):
    result = await db.execute(select(Warehouse).where(Warehouse.id == warehouse_id))
    return result.scalars().first()


# Создать новый склад
async def create_warehouse(db: AsyncSession, warehouse: WarehouseCreate):
    db_warehouse = Warehouse(**warehouse.dict())
    db.add(db_warehouse)
    await db.commit()
    await db.refresh(db_warehouse)
    return db_warehouse


# Обновить информацию о складе
async def update_warehouse(db: AsyncSession,  warehouse_id: int,  warehouse:  WarehouseUpdate):
    stmt = (
        update(Warehouse).
        where(Warehouse.id == warehouse_id).
        values(**warehouse.dict(exclude_unset=True)).
        returning(Warehouse)
    )
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()


# Удалить склад
async def delete_warehouse(db: AsyncSession, warehouse_id: int):
    stmt = delete(Warehouse).where(Warehouse.id == warehouse_id).returning(Warehouse)
    result = await db.execute(stmt)
    await db.commit()
    return result.scalars().first()

