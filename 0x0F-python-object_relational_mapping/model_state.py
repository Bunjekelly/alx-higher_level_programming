#!/usr/bin/python3

"""a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State Class that inherits from Base"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
