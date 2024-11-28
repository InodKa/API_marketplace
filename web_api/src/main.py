# src/main.py

from fastapi import FastAPI
from src.dao.database import engine
from src.dao import models
from src.routers import users

import uvicorn

app = FastAPI(title="Marketplace API")

# Включение маршрутов
app.include_router(users.router)

# Создание таблиц при старте приложения
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Эндпоинт для проверки состояния приложения
@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
