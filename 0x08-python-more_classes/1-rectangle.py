#!/usr/bin/python3

""" Rectangle class definition """


class Rectangle:
    """Rectangle class with setters and getters for its private variable"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter to retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to set new width attribute to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter to retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set height attribute to width"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
