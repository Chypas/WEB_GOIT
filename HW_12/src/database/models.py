import enum

from sqlalchemy import Column, Integer, String, DateTime, func, Date, Enum
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Role(enum.Enum):
    admin: str = 'admin'
    user: str = 'user'


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    birthday = Column(Date)
    description = Column(String)

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)
    role = Column('role', Enum(Role), default=Role.user)
