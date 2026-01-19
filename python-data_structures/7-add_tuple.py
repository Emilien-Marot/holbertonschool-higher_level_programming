#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t1 = tuple_2(tuple_a)
    t2 = tuple_2(tuple_b)
    return (t1[0]+t2[0], t1[1]+t2[1])


def tuple_2(my_tuple):
    if len(my_tuple) == 0:
        return (0, 0)
    elif len(my_tuple) == 1:
        return (my_tuple[0], 0)
    else:
        return (my_tuple[0], my_tuple[1])
