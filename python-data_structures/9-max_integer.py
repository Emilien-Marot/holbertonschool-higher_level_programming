#!/usr/bin/python3
def max_integer(my_list=[]):
    res = None
    for i in my_list:
        if res == None or i > res:
            res = i
    return res
