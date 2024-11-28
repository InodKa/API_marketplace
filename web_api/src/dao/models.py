from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Text, TIMESTAMP, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.schema import UniqueConstraint

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False, index=True)
    phone = Column(String(12), nullable=False, unique=True)

    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(SmallInteger, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)

    orders = relationship("Order", back_populates="status")
    transfers = relationship("Transfer", back_populates="status")

class PickupPoint(Base):
    __tablename__ = 'pickup_points'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, unique=True, nullable=False)
    phone = Column(String(12), nullable=False, unique=True)

    orders = relationship("Order", back_populates="pickup_point")
    transfers = relationship("Transfer", back_populates="to_pickup_point")

class Warehouse(Base):
    __tablename__ = 'warehouses'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(Text, unique=True, nullable=False)
    phone = Column(String(12), nullable=False, unique=True)

    inventories = relationship("Inventory", back_populates="warehouse")
    transfers_from = relationship("Transfer", back_populates="from_warehouse")

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    name = Column(String(150), unique=True, nullable=False)

    subcategories = relationship("Category", backref='parent', remote_side=[id])
    products = relationship("Product", back_populates="category")

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), unique=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    description = Column(Text, nullable=True)

    category = relationship("Category", back_populates="products")
    order_items = relationship("OrderItem", back_populates="product")
    inventories = relationship("Inventory", back_populates="product")
    transfers = relationship("Transfer", back_populates="product")

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    pickup_point_id = Column(Integer, ForeignKey('pickup_points.id', ondelete='CASCADE'), nullable=False)
    total_cost = Column(DECIMAL(10, 2), nullable=False)
    status_id = Column(SmallInteger, ForeignKey('statuses.id'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="orders")
    pickup_point = relationship("PickupPoint", back_populates="orders")
    status = relationship("Status", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")

class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    count = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product", back_populates="order_items")

class Inventory(Base):
    __tablename__ = 'inventories'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    warehouse_id = Column(Integer, ForeignKey('warehouses.id'), nullable=False)
    count = Column(Integer, nullable=False)

    product = relationship("Product", back_populates="inventories")
    warehouse = relationship("Warehouse", back_populates="inventories")

    __table_args__ = (
        # Уникальность комбинации product_id и warehouse_id
        UniqueConstraint('product_id', 'warehouse_id', name='uix_product_warehouse'),
    )

class Transfer(Base):
    __tablename__ = 'transfers'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    from_warehouse_id = Column(Integer, ForeignKey('warehouses.id'), nullable=False)
    to_pickup_point_id = Column(Integer, ForeignKey('pickup_points.id'), nullable=False)
    status_id = Column(SmallInteger, ForeignKey('statuses.id'), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    order = relationship("Order")
    product = relationship("Product", back_populates="transfers")
    from_warehouse = relationship("Warehouse", back_populates="transfers_from")
    to_pickup_point = relationship("PickupPoint", back_populates="transfers")
    status = relationship("Status", back_populates="transfers")
