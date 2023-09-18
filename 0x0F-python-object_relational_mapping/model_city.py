#!/usrr/bin/python3

""" a Python file model_city.py that contains the class definition of a City"""

from model_state import Base, State
from sqlalchemy import Integer, String, Column, ForeignKey


class City(Base):
    """city class"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("States.id"), nullable=False)
