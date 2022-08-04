#!/usr/bin/python3

"""
Function to add a new attribute an object if possible
"""


def add_attribute(obj, name, value):
    """attribute assignment"""
    if hasattr(obj, '__dict__') or name in getattr(obj, '__slots__', {}):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
