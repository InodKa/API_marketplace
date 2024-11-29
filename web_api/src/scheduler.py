from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from datetime import datetime, timedelta
from sqlalchemy.future import select
import asyncio
import json
from dao.database import async_session
from dao.models import User  # Импортируйте нужные модели
import os

# Путь для сохранения файлов
EXPORT_DIRECTORY = os.getenv("EXPORT_DIRECTORY", "/export")

async def export_new_records():
    async with async_session() as session:
        # Пример: экспорт новых пользователей за последнюю минуту
        one_minute_ago = datetime.utcnow() - timedelta(minutes=1)
        result = await session.execute(
            select(User).where(User.created_at >= one_minute_ago)
        )
        new_users = result.scalars().all()
        
        if new_users:
            data = [user.to_dict() for user in new_users]  # Реализуйте метод to_dict в модели
            filename = datetime.utcnow().strftime("users_%Y%m%d%H%M%S.json")
            filepath = os.path.join(EXPORT_DIRECTORY, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            
            print(f"Exported {len(new_users)} users to {filepath}")

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        export_new_records,
        trigger=IntervalTrigger(minutes=1),
        id='export_new_records',
        name='Export new records every minute',
        replace_existing=True
    )
    scheduler.start()
