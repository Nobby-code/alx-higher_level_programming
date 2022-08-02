#!/usr/bin/python3
"""
module to check if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    function with two arguments: obj, a_class:
        obj is the object
        a_class is the instance
    """
    if (type(obj) == a_class):
        # the object is exactly an instance of the a_class
        return True
    # if not
    return False
