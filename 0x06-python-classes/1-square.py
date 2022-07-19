"""Class with private member
    Only accessible within the class
"""


class Square:
    """Private member size initialized"""
    def __init__(self, size):
        """Initialization of the method"""
        self.__size = size
