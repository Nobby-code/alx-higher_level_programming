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
    """
    area(): returns self.size * self.size
    """
    def area(self):
        return self.__size * self.__size
