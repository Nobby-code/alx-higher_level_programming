#!/usr/bin/python3
"""class Square with default size"""


class Square:
    """
    initialization def
        Args: integer size
        Raises TyeError if size not an integer
        Raises ValueError if size < 0
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter for private instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter to set the __size to value
        checks if value is integer, if not:
            raise TypeError
        if value < 0:
            reaise ValueError

        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        area():
            returns self.size * self.size
        """
        return self.__size * self.__size

    def my_print(self):
        """printing # in place of a square number"""
        for value1 in range(self.__size):
            for value2 in range(self.__size):
                print("#", end="")
            print()
        if not self.__size:
            print()
