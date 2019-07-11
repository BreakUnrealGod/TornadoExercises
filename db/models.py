from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float

from db.connect import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(15), unique=True)
    password = Column(String(15))
    createtime = Column(DateTime, default=datetime.now)

    def __str__(self):
        return self.username


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    bname = Column(String(15), unique=True)
    price = Column(Float)

    def __str__(self):
        return self.bname


if __name__ == '__main__':
    Base.metadata.create_all()
