#!/usr/bin/python3

def safe_print_integer(value):
    """
    Try/Except to print only if value is an integer
    Else it warns you tha the value is not integer
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        return False
    else:
        return True
