#!/usr/bin/python3
import sys


def place_queen(list_queen_init, line, size):
    for col in range(0, size):
        valid = True
        for queen in list_queen_init:
            diff_line = abs(line - queen[0])
            diff_col = abs(col - queen[1])
            if diff_line == diff_col:
                valid = False
                break
            if diff_line == 0 or diff_col == 0:
                valid = False
                break
        if not valid:
            continue
        list_queen = list_queen_init[:]
        list_queen.append([line, col])
        if line == size - 1:
            print(list_queen)
        else:
            place_queen(list_queen, line + 1, size)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    size = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)
if size < 4:
    print("N must be at least 4")
    exit(1)
place_queen([], 0, size)
