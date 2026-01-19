#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        sep = ""
        for i in line:
            print("{}{:d}".format(sep, i), end="")
            sep = " "
        print("")
