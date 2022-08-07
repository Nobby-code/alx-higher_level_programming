#!/usr/bin/python3

"""
Square class that inherits from Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        Square class initialization
        """
        self.size = size

        # inheriting from parent class
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter - to retrieve
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        size setter - set the size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the square information
        """

        square_info = "[Square] "
        square_info += "({}) ".format(self.id)
        square_info += "{:d}/{:d} - ".format(self.x, self.y)
        square_info += "{:d}".format(self.size)

        return square_info

    def update(self, *args, **kwargs):
        """
        updating the square class
        """
        index = 0
        if args is not None and len(args) != 0:

            for argument in args:
                index += 1
                if index == 1:
                    self.id = argument
                elif index == 2:
                    self.size = argument
                elif index == 3:
                    self.x = argument
                elif index == 4:
                    self.y = argument

        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        Returning dictionary representation of a square
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
