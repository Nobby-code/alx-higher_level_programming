#!/usr/bin/python3
"""Sequare class importation"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    class
    """

    def __init__(self, size):
        """
        init constructor
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
    
    def area(self):
        """
        area() method implementation
        """
        return self.__size * self.__size
