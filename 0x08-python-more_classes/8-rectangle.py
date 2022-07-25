#!/usr/bin/python3

"""Rectangle class printing #"""


class Rectangle:
    """Rectangle class"""

    # class attribute
    number_of_instances = 0

    # class attribute
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter to set the width to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter to set height to value"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Methos to return the area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Method to return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return 2 * (self.__width + self.__height)

    # using __str__
    def __str__(self):
        """Converting to string format"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        # using print_symbol
        h = ((str(self.print_symbol) * self.__width) + "\n") * self.__height
        return h[:-1]

    # prints unambiguous output
    def __repr__(self):
        """Returning a string representation of an object"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    # calling destructor method
    def __del__(self):
        """Destructor method - called when an object is deleted"""

        # decrementing number each time of deletion
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    # creating static method
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return (rect_2)
        return (rect_1)
