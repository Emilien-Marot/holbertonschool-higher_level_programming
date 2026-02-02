#!/usr/bin/python3
'''
Docstring for python-inheritance.0-lookup
'''


def is_same_class(obj, a_class):
    '''
    Docstring for is_same_class
    :param obj: Description
    :param a_class: Description
    '''
    return type(obj).__name__ == a_class.__name__
