#!/usr/bin/python3

""" Rectangle class importation """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherites from 
    Rectangle class
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
    
    def __str__(self):
        """
        Inbuils __str__ to print string format
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
