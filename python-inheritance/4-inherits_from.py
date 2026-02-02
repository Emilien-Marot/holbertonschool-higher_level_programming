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
    type_obj = type(obj)
    name_type = type_obj.__name__
    return name_type != a_class.__name__ and issubclass(type_obj, a_class)
