#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_2 = matrix[:]
    for i in range(0, len(matrix)):
        matrix_2[i] = matrix_2[i][:]
        for j in range(0, len(matrix[i])):
            matrix_2[i][j] = matrix[i][j]**2
    return matrix_2
