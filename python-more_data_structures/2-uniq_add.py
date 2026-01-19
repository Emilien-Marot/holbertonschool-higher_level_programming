#!/usr/bin/python3
def uniq_add(my_list=[]):
    finished = []
    res = 0
    for i in my_list:
        if i not in finished:
            res += i
            finished.append(i)
    return res
