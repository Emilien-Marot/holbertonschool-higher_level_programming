#!/usr/bin/python3
def pow(a, b):
    res = 1
    if b > 0:
        for i in range(0, b):
            res *= a
    elif b < 0:
        for i in range(b, 0):
            res /= a
    return res
