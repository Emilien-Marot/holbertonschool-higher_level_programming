#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    arg_end = "s:"
    if len(argv) == 1:
        arg_end = '.'
    elif len(argv) == 2:
        arg_end = ':'
    print("{} argument{}".format(len(argv) - 1, arg_end))
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
