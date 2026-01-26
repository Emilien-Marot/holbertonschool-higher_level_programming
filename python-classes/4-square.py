#!/usr/bin/python3
'''
godzilla vs king kong - ERB
'''


class Square:
    '''
    Docstring for Square 2: Electric Boogaloo
    '''
    def __init__(self, size=0):
        '''were you expecting serious comments ?'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.size**2
