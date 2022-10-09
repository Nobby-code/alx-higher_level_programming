#!/usr/bin/python3

"""
Class definition of City that inherits from Base -> declarative
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#Base = declarative_base()
from model_state import Base, State
""" 
Instance Base -> City inherits from
"""


class City(Base):
    """City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
