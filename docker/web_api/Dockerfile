# docker/web_api/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY ../../web_api/src /app

# Установка PYTHONPATH
ENV PYTHONPATH=/app

# Запуск приложения с использованием Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
