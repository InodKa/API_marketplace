from fastapi import FastAPI
from routers import users
# Импортируйте другие роутеры аналогично

app = FastAPI(
    title="Marketplace API",
    description="API для управления маркетплейсом",
    version="1.0.0"
)

app.include_router(users.router)
# Подключите другие роутеры аналогично

# Инициализация базы данных при старте приложения
@app.on_event("startup")
async def on_startup():
    from dao.database import engine, Base
    async with engine.begin() as conn:
        # Создание всех таблиц
        await conn.run_sync(Base.metadata.create_all)
