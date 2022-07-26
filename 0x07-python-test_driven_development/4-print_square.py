#!/usr/bin/python3

""" Print square module """


def print_square(size):
    """
    def print_square(size):
        size must be an integer
        size must not be less than 0
        Raises:
            ValueError if size is less than 0
            TypeError if size is not an integer
        Squares the size and print # in place of the result

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
