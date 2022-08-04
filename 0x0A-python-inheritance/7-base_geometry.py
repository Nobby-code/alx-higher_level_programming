#!/usr/bin/python3
"""
BaseGeometry class
"""


class BaseGeometry:
    """area() method raises Exception"""
    def area(self):
        """
        area method raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
