#!/usr/bin/python3
'''
Docstring for python-inheritance.0-lookup
'''


def inherits_from(obj, a_class):
    '''
    Docstring for is_same_class
    :param obj: Description
    :param a_class: Description
    '''
    return type(obj).__name__ != a_class.__name__ and issubclass(type(obj), a_class)
