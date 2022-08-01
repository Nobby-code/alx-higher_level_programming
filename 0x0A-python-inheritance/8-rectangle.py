#!/usr/bin/python3


"""parent class"""


class BaseGeometry:
    """BaseGeometry is parent class"""
    def area(self):
        """area method that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validato method for same and value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


"""sub class"""


class Rectangle(BaseGeometry):
    """
    Rectangle class which inherites from BaseGeometry
    class
    """
    def __init__(self, width, height):
        """
        init constructor
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
