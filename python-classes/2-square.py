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
        self.__size = size
