#!/usr/bin/python3
'''
want some comments?
'''


def add_integer(a, b=98):
    '''
    here you go
    '''
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except:
        raise TypeError("b must be an integer")
    return a + b
