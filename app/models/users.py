# models.py
from sqlalchemy import Column, Integer, String
from models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer)