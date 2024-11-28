from sqlalchemy import Column, Integer, String, SmallInteger
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    middle_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=False)
    email = Column(String(50), unique=True, nullable=False, index=True)
    phone = Column(String(12), nullable=False)


class Status(Base):
    __tablename__ = "statuses"

    id = Column(SmallInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)




