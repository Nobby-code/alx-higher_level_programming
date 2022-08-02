#!/usr/bin/python3
"""parent class"""


class BaseGeometry:

    """area not implemented"""
    def area(self):
        raise Exception("area() is not implemented")

    """validator"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < 1:
            raise ValueError("{} must be greater than 0".format(name))


"""sub class"""


class Rectangle(BaseGeometry):
    """__init__ for validation - to validate height and width"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """calculating the area"""
    def area(self):
        return self.__width * self.__height

    """printing the string"""
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
