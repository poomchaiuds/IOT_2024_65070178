from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

from database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    year = Column(Integer, index=True)
    is_published = Column(Boolean, index=True)

class Coffee(Base):
    __tablename__ = 'coffees'

    c_id = Column(Integer, primary_key=True)
    c_title = Column(String)
    c_price = Column(Integer)