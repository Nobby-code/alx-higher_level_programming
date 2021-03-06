#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    my_args = argv[1:]
    arg_length = len(argv) - 1
    operators = ["+", "-", "*", "/"]

    if arg_length != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
        elif argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print("{:d} + {:d} = {:d}".format(a, b, sum(a, b)))
        elif argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        elif argv[2] not in operators:
            print("Unkown operator. Available operators: +, -, * and /")
            exit(1)
