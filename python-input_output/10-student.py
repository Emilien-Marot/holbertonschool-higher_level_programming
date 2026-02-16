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

    def to_json(self, attrs=None):
        '''
        Docstring for to_json

        :param self: Description
        '''
        if attrs is None:
            return self.__dict__
        res = {}
        for key in self.__dict__.keys():
            if key in attrs:
                res.update({key: self.__dict__[key]})
        return res
