#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    my_args = argv[1:]

    result = 0

    for a in my_args:
        result += int(a)
    print("{:d}".format(result))
