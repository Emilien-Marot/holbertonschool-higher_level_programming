#!/usr/bin/python3
for char in range(97, 123):
    if char not in (101, 112):
        print("{}".format(chr(char)), end="")
