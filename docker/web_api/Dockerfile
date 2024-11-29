# docker/web_api/Dockerfile

FROM python:3.11-slim

# Установка зависимостей
WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY web_api/src /app

# Создание директории для экспорта
RUN mkdir -p /export

# Установка переменной окружения по умолчанию (если не установлена через docker-compose)
ENV EXPORT_DIRECTORY=/export

# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
