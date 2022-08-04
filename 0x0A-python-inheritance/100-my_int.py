#!/usr/bin/python3

"""
class MyInt
"""


class MyInt(int):
    """
    class for the rebel
    """
    def __eq__(self, other):
        """Return True if self and other not equal, else false"""
        return int(self) != other

    def __ne__(self, other):
        """Return True if self and other equal, else false"""
        return int(self) == other
