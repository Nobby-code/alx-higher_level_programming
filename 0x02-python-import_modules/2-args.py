#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_length = len(argv) - 1

    i = 1

    if arg_length == 0:
        print("{:d} arguments.".format(arg_length))
    elif arg_length == 1:
        print("{:d} argument:".format(arg_length))
        print("{:d}: {:s}".format(i, argv[i]))
    else:
        print("{:d} arguments:".format(arg_length))
        while i <= arg_length:
            print("{:d}: {:s}".format(i, argv[i]))
            i = i + 1
