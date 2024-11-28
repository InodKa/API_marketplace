-- Таблица пользователей
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    phone VARCHAR(12) UNIQUE,
    CONSTRAINT chk_phone CHECK (phone ~ '^\+7\d{10}$')
);

-- Таблица статусов
CREATE TABLE IF NOT EXISTS statuses (
    id SMALLSERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- Таблица пунктов самовывоза
CREATE TABLE IF NOT EXISTS pickup_points (
    id SERIAL PRIMARY KEY,
    address TEXT NOT NULL UNIQUE,
    phone VARCHAR(12) NOT NULL UNIQUE, 
    CONSTRAINT chk_phone CHECK (phone ~ '^\+7\d{10}$')
);

-- Таблица складов
CREATE TABLE IF NOT EXISTS warehouses (
    id SERIAL PRIMARY KEY,
    address TEXT NOT NULL UNIQUE,
    phone VARCHAR(12) NOT NULL UNIQUE,
    CONSTRAINT chk_phone CHECK (phone ~ '^\+7\d{10}$')
);

-- Таблица категорий продуктов
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    parent_id INTEGER,
    name VARCHAR(150) NOT NULL UNIQUE,
    FOREIGN KEY (parent_id) REFERENCES categories(id)
);

-- Таблица продуктов
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    category_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Таблица заказов
CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    pickup_point_id INTEGER NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL CHECK (total_cost >= 0),
    status_id SMALLINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (pickup_point_id) REFERENCES pickup_points(id) ON DELETE CASCADE,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);

-- Таблица связей заказов и продуктов (order_items)
CREATE TABLE IF NOT EXISTS order_items (
	id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    count INTEGER NOT NULL CHECK (count > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Таблица инвентаризации на складах
CREATE TABLE IF NOT EXISTS inventories (
    id SERIAL PRIMARY KEY,
    product_id INTEGER NOT NULL,
    warehouse_id INTEGER NOT NULL,
    count INTEGER NOT NULL CHECK (count >= 0),
    UNIQUE (product_id, warehouse_id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (warehouse_id) REFERENCES warehouses(id)
);

-- Таблица трансферов
CREATE TABLE IF NOT EXISTS transfers (
    id SERIAL PRIMARY KEY,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    from_warehouse_id INTEGER NOT NULL,
    to_pickup_point_id INTEGER NOT NULL,
    status_id SMALLINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (from_warehouse_id) REFERENCES warehouses(id),
    FOREIGN KEY (to_pickup_point_id) REFERENCES pickup_points(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);