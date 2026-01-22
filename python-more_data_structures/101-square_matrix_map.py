#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda ln: list(map(lambda x: x*x, ln[:])), matrix[:]))
