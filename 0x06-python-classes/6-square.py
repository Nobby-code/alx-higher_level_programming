#!/usr/bin/python3
"""class Square with default size"""


class Square:
    """
    initialization def
        Args: integer size
        Raises TyeError if size not an integer
        Raises ValueError if size < 0
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter for a poition private instance"""
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter to set __position to value
        if position not a tuple of 2 integere:
            raise TypeError exception with a message
        """
        # if type(value) is tuple and len(value) == 2:
        #     if type(value[0]) is not int or value[0] < 0\
        #     or type(value[1]) is not int or value[1] < 0:
        #         raise TypeError with message
        #     else:
        #         self.__position = value

        if value is not tuple or len(value) != 2 or\
                type(value[0]) is not int or value[0] < 0 or\
                type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        area():
            returns self.size * self.size
        """
        return self.__size * self.__size

    def my_print(self):
        """printing # in place of a number to the stdout"""

        if self.size == 0:
            print("")
        else:
            for row in range(self.size):
                print(" " * self.position[0], end="")
                for col in range(self.size):
                    print("#", end="")
                print("")
