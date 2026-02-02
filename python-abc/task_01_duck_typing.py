#!/usr/bin/python3
'''
Docstring for python-abc.task_00_abc
'''
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    '''
    Docstring for Shape
    '''
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    '''
    Docstring for Circle
    '''
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        if self.__radius < 0:
            print(self.__radius) 
        return pi * self.__radius * self.__radius

    def perimeter(self):
        return pi * 2 * self.__radius


class Rectangle(Shape):
    '''
    Docstring for Rectangle
    '''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


def shape_info(shape):
    '''
    Docstring for shape_info
    :param shape: Description
    '''
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
