#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


class Student:
    '''
    Docstring for read_file
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :param last_name: Description
        :param age: Description
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        Docstring for to_json

        :param self: Description
        '''
        return self.__dict__
