#!/usr/bin/python3
'''
Docstring for python-abc.task_00_abc
'''


class CountedIterator:
    '''
    Docstring for CountedIterator
    '''
    def __init__(self, object):
        self.object = iter(object)
        self.counter = 0

    def __next__(self):
        self.counter += 1
        return next(self.object)

    def get_count(self):
        return self.counter
