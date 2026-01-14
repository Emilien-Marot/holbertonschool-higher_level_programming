#!/usr/bin/python3
def remove_char_at(string, n):
    res = ""
    for i in range(0, len(string)):
        if i != n:
            res += string[i]
    return res
