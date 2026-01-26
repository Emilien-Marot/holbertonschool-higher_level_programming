#!/usr/bin/python3
'''
godzilla vs king kong - ERB
'''


class Square:
    '''
    Docstring for Square 2: Electric Boogaloo
    '''
    def __init__(self, size=0, position=(0, 0)):
        '''were you expecting serious comments ?'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.position = position
        self.size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for pos in position:
            if not isinstance(pos, int) or pos < 0:
                raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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

    def my_print(self):
        if self.size == 0:
            print("")
            return
        for buf in range(0, self.position[1]):
            print("")
        for i in range(0, self.size):
            for buf in range(0, self.position[0]):
                print(" ", end="")
            for j in range(0, self.size):
                print("#", end="")
            print("")
