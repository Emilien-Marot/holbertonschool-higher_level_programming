#!/usr/bin/python3
"""
This is a module-level docstring.
It describes the purpose of the entire script/module.
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    '''
    Docstring for the class
    '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id
