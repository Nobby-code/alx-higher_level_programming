#!/usr/bin/python3

""" Addition of two integers
Function takes two inputs - a and b
Checks if they are integers or floats, then add them
else raise TypeError
"""


def add_integer(a, b=98):
    """Function to add two integer values
    add_integer: int a + int b (floats typecasted to integer)
        raise TypeError - if a or b is not an integer or a float
    return a + b
    """
    if type(a) is not float and type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not float and type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
