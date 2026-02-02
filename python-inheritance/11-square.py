#!/usr/bin/python3
'''
Docstring for python-inheritance.8-rectangle
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    Docstring for Square
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return super().area()

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
