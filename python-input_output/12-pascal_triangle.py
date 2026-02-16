#!/usr/bin/python3
'''
Docstring for python-input_output.0-read_file
'''


def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    for i in range(0, n):
        if i == 0:
            triangle.append([1])
        else:
            triangle.append(pascal_line(triangle[i-1]))
    return triangle


def pascal_line(line_up):
    line = [line_up[0]]
    for i in range(1, len(line_up)):
        line.append(line_up[i]+line_up[i-1])
    line.append(line_up[len(line_up)-1])
    return line
