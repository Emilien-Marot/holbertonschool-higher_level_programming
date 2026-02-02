#!/usr/bin/python3
'''
Docstring for python-inheritance.5-base_geometry
'''


class BaseGeometry:
    '''
    Docstring for BaseGeometry
    '''
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value).__name__ != int.__name__:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True
