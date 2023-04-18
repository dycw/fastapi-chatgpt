from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class Item(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
