#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul
    if len(argv) == 4:
        op = argv[2]
        if argv[2] in ("+","-","*","/"):
            a = int(argv[1])
            b = int(argv[3])
            if op == "+":
                res = add(a,b)
            elif op == "-":
                res = sub(a,b)
            elif op == "*":
                res = mul(a,b)
            else:
                res = div(a,b)
            print(f"{a} {op} {b} = {res}")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>");
        exit(1)
