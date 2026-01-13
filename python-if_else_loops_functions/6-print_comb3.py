#!/usr/bin/python3
first = True
for i in range(0, 9):
    for j in range(i + 1, 10):
        if first:
            first = False
        else:
            print(", ", end="")
        print("{}{}".format(i, j), end="")
print("")
