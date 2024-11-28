from fastapi import FastAPI
from routers import users, statuses, pickup_points, warehouses


app = FastAPI(
    title="Marketplace API",
    description="API для управления маркетплейсом",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(statuses.router)
app.include_router(pickup_points.router)
app.include_router(warehouses.router)


# Инициализация базы данных при старте приложения
@app.on_event("startup")
async def on_startup():
    from dao.database import engine, Base
    async with engine.begin() as conn:
        # Создание всех таблиц
        await conn.run_sync(Base.metadata.create_all)
