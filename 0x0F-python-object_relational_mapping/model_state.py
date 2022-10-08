#!/usr/bin/python3

"""
Class definition of State that inherits from Base -> declarative
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
""" Instance """


class State(Base):
    """State Class
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
