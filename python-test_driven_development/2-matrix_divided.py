#!/usr/bin/python3
'''
and one comment
'''


def matrix_divided(matrix, div):
    '''
    and another one
    '''
    len_line = None
    err = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(err)
    for line in matrix:
        if not isinstance(matrix, list):
            raise TypeError(err)
        if len_line is None:
            len_line = len(line)
        elif len_line != len(line):
            raise TypeError("Each row of the matrix must have the same size")
        new_line = []
        for cell in line:
            if not isinstance(cell, (int, float)):
                raise TypeError(err)
            new_line.append(round(cell/div, 2))
        new_matrix.append(new_line[:])
    return new_matrix
