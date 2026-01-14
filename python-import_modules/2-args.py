#!/usr/bin/python3
from sys import argv
if len(argv) < 2:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")
