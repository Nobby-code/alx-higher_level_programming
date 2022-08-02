#!/usr/bin/python3
"""parent class"""


class BaseGeometry:
    """area not implemented"""
    def area(self):
        """area method that raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


"""sub class"""


class Rectangle(BaseGeometry):
    """
    Rectangle class which inherites from BaseGeometry
    class
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
