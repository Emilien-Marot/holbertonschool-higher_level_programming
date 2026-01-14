#!/usr/bin/python3
for num in range(0, 26):
    upper_a = ord("A")
    lower_a = ord("a")
    if num % 2 == 0:
        char = chr(25 + lower_a - num)
    else:
        char = chr(25 + upper_a - num)
    print("{}".format(char), end="")
