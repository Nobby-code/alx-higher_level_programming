"""Class with private member
    Only accessible within the class
"""


class Square:
    """Private member size initialized"""
    def __init__(self, size):
        self.__size = size
