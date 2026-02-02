#!/usr/bin/python3
'''
Docstring for python-inheritance.0-lookup
'''


class MyList(list):
    '''
    Docstring for Mylist
    '''
    def print_sorted(self):
        new = self[:]
        new.sort()
        print(new)
