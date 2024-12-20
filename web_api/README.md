# Эндпоинты и Описание

## 1. Пользователи (`/users`)
- `GET /users`
  - **Описание**: Получить список всех пользователей
  - **Цель**: Позволяет администратору или другим сервисам получать информацию о зарегистрированных пользователях

- `GET /users/{id}`
  - **Описание**: Получить информацию о конкретном пользователе по ID
  - **Цель**: Предоставляет детальную информацию о пользователе

- `POST /users`
  - **Описание**: Создать нового пользователя
  - **Цель**: Регистрация нового пользователя в системе

- `PUT /users/{id}`
  - **Описание**: Обновить информацию о пользователе
  - **Цель**: Позволяет изменять данные пользователя, такие как имя, email и телефон

- `DELETE /users/{id}`
  - **Описание**: Удалить пользователя
  - **Цель**: Удаление учетной записи пользователя из системы

## 2. Статусы (`/statuses`)
- `GET /statuses`
  - **Описание**: Получить список всех статусов
  - **Цель**: Используется для отображения возможных статусов заказов и трансферов

- `GET /statuses/{id}`
  - **Описание**: Получить информацию о конкретном статусе
  - **Цель**: Детальная информация о статусе по его ID

- `POST /statuses`
  - **Описание**: Создать новый статус
  - **Цель**: Добавление новых статусов для заказов или трансферов

- `DELETE /statuses/{id}`
  - **Описание**: Удалить статус
  - **Цель**: Удаление статуса из системы

## 3. Пункты Самовывоза (`/pickup_points`)
- `GET /pickup_points`
  - **Описание**: Получить список всех пунктов самовывоза
  - **Цель**: Отображение доступных мест для получения заказов

- `GET /pickup_points/{id}`
  - **Описание**: Получить информацию о конкретном пункте самовывоза
  - **Цель**: Детальная информация о пункте по его ID

- `POST /pickup_points`
  - **Описание**: Создать новый пункт самовывоза
  - **Цель**: Добавление новых мест для самовывоза заказов

- `PUT /pickup_points/{id}`
  - **Описание**: Обновить информацию о пункте самовывоза
  - **Цель**: Изменение адреса, телефона или других данных пункта

- `DELETE /pickup_points/{id}`
  - **Описание**: Удалить пункт самовывоза
  - **Цель**: Удаление пункта из системы

## 4. Склады (`/warehouses`)
- `GET /warehouses`
  - **Описание**: Получить список всех складов
  - **Цель**: Отображение доступных складских помещений для инвентаризации

- `GET /warehouses/{id}`
  - **Описание**: Получить информацию о конкретном складе
  - **Цель**: Детальная информация о складе по его ID

- `POST /warehouses`
  - **Описание**: Создать новый склад
  - **Цель**: Добавление новых складских помещений в систему

- `PUT /warehouses/{id}`
  - **Описание**: Обновить информацию о складе
  - **Цель**: Изменение адреса, телефона или других данных склада

- `DELETE /warehouses/{id}`
  - **Описание**: Удалить склад
  - **Цель**: Удаление склада из системы

## 5. Категории Продуктов (`/categories`)
- `GET /categories`
  - **Описание**: Получить список всех категорий продуктов
  - **Цель**: Отображение структуры категорий для фильтрации и поиска продуктов

- `GET /categories/{id}`
  - **Описание**: Получить информацию о конкретной категории
  - **Цель**: Детальная информация о категории по ее ID

- `POST /categories`
  - **Описание**: Создать новую категорию
  - **Цель**: Добавление новых категорий или подкатегорий в систему

- `PUT /categories/{id}`
  - **Описание**: Обновить информацию о категории
  - **Цель**: Изменение названия или родительской категории

- `DELETE /categories/{id}`
  - **Описание**: Удалить категорию
  - **Цель**: Удаление категории из системы

## 6. Продукты (`/products`)
- `GET /products`
  - **Описание**: Получить список всех продуктов
  - **Цель**: Отображение доступных продуктов для покупки

- `GET /products/{id}`
  - **Описание**: Получить информацию о конкретном продукте
  - **Цель**: Детальная информация о продукте по его ID

- `POST /products`
  - **Описание**: Создать новый продукт
  - **Цель**: Добавление новых продуктов в каталог

- `PUT /products/{id}`
  - **Описание**: Обновить информацию о продукте
  - **Цель**: Изменение названия, цены, описания или категории продукта

- `DELETE /products/{id}`
  - **Описание**: Удалить продукт
  - **Цель**: Удаление продукта из каталога

## 7. Заказы (`/orders`)
- `GET /orders`
  - **Описание**: Получить список всех заказов
  - **Цель**: Отображение всех заказов, их статусов и деталей

- `GET /orders/{id}`
  - **Описание**: Получить информацию о конкретном заказе
  - **Цель**: Детальная информация о заказе по его ID

- `POST /orders`
  - **Описание**: Создать новый заказ
  - **Цель**: Оформление заказа пользователем

- `PUT /orders/{id}`
  - **Описание**: Обновить информацию о заказе
  - **Цель**: Изменение статуса заказа или других деталей

- `DELETE /orders/{id}`
  - **Описание**: Удалить заказ
  - **Цель**: Отмена заказа и удаление его из системы

## 8. Элементы Заказа (`/orders/{order_id}/items`)
- `GET /orders/{order_id}/items`
  - **Описание**: Получить список всех элементов заказа
  - **Цель**: Отображение продуктов, входящих в заказ

- `POST /orders/{order_id}/items`
  - **Описание**: Добавить элемент в заказ
  - **Цель**: Добавление продукта к заказу

- `PUT /orders/{order_id}/items/{item_id}`
  - **Описание**: Обновить элемент заказа
  - **Цель**: Изменение количества или цены продукта в заказе

- `DELETE /orders/{order_id}/items/{item_id}`
  - **Описание**: Удалить элемент из заказа
  - **Цель**: Удаление продукта из заказа

## 9. Инвентаризация (`/inventories`)
- `GET /inventories`
  - **Описание**: Получить список всех записей инвентаризации
  - **Цель**: Отображение наличия продуктов на складах

- `GET /inventories/{id}`
  - **Описание**: Получить информацию о конкретной записи инвентаризации
  - **Цель**: Детальная информация о наличии продукта на складе

- `POST /inventories`
  - **Описание**: Создать новую запись инвентаризации
  - **Цель**: Добавление нового продукта на склад или обновление существующего

- `PUT /inventories/{id}`
  - **Описание**: Обновить информацию о инвентаризации
  - **Цель**: Изменение количества продукта на складе

- `DELETE /inventories/{id}`
  - **Описание**: Удалить запись инвентаризации
  - **Цель**: Удаление продукта со склада

## 10. Трансферы (`/transfers`)
- `GET /transfers`
  - **Описание**: Получить список всех трансферов
  - **Цель**: Отображение всех операций по перемещению товаров

- `GET /transfers/{id}`
  - **Описание**: Получить информацию о конкретном трансфере
  - **Цель**: Детальная информация о трансфере по его ID

- `POST /transfers`
  - **Описание**: Создать новый трансфер
  - **Цель**: Инициация перемещения товара со склада в пункт самовывоза

- `PUT /transfers/{id}`
  - **Описание**: Обновить информацию о трансфере
  - **Цель**: Изменение статуса трансфера или других деталей

- `DELETE /transfers/{id}`
  - **Описание**: Удалить трансфер
  - **Цель**: Отмена операции перемещения товара