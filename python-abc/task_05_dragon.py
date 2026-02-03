#!/usr/bin/python3
'''
Docstring for python-abc.task_00_abc
'''


class SwimMixin:
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''
    Docstring for CountedIterator
    '''
    def roar(self):
        print("The dragon roars!")
