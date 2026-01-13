#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) in range (ord("a"), ord("z") + 1):
            num = ord(char) + (ord("A") - ord("a"))
        else:
            num = ord(char)
        print("{}".format(chr(num)), end="")
    print("")
