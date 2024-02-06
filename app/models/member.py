from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(18), nullable=False, unique=True)
    passwd = Column(String(18), nullable=False)
    name = Column(String(10), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    regdate = Column(DateTime, default=datetime.now)