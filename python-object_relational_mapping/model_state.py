#!/usr/bin/python3
"""
This is a module-level docstring.
It describes the purpose of the entire script/module.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()


class State(Base):
    '''
    Docstring for the class
    '''
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
