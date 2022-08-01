#!/usr/bin/python3

"""BaseGeometry class"""


class BaseGeometry:
    """area() method raises Exception"""
    def area(self):
        raise Exception("area() is not implemented")
    
    """validator too validate name and value"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))
