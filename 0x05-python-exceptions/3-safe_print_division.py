#!/usr/bin/python3

def safe_print_division(a, b):

    """
    Try to  print division of a b
    except to check for ZeroDivisionException

    """
    result = 0
    try:
        result = result + (a / b)
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
