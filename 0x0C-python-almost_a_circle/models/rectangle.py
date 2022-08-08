#!/usr/bin/python3

from models.base import Base
"""
Rectangle class
"""


class Rectangle(Base):
    """
    class Rectangle:
        with private instance variables
        with setters and getters for the variables
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # inheriting the parent constructor properties
        super().__init__(id)

    @property
    def width(self):
        """width getter to return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter to set the value
        Exceptions:
            raises TypeError: if width is not integer
            raises ValueError: if width < 1
        Assigns width to value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        Exceptions:
            raises TypeError: if height is not integer
            raises ValueError: if height < 1
        Assigns height to value

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for x
        Exceptions:
            raises TypeError: if x is not integer
            raises ValueError: if x < 0
        Assigns x to value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        def area(self):
            return area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        def display(self):
            prints out the rectangle instance with the character #
        """
        for m in range(self.y):
            print()
        for i in range(self.height):
            for n in range(self.width):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        inbuilt function to return the rectangle properties
        """

        my_str = "[Square] "
        my_str += "({}) ".format(self.id)
        my_str += "{:d}/{:d} - ".format(self.x, self.y)
        my_str += "{:d}/{:d}".format(self.width, self.height)

        return my_str

    def update(self, *args, **kwargs):
        """
        def update(self, *args):
            function that assigns argument to each attribute

            later update its arguments:
            def update(self, *args, **kwargs)
        """
        arg_len = 0
        if args is not None and len(args) != 0:
            for argument in args:
                arg_len += 1
                if arg_len == 1:
                    self.id = argument
                elif arg_len == 2:
                    self.__width = argument
                elif arg_len == 3:
                    self.__height = argument
                elif arg_len == 4:
                    self.__x = argument
                elif arg_len == 5:
                    self.__y = argument
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Returning the dictionary representation of a rectangle
        """
        my_dict = {}

        for element in ["id", "width", "height", "x", "y"]:
            my_dict[element] = getattr(self, element)

        return my_dict
