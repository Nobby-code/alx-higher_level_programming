#!/usr/bin/python3

"""
class MyInt
"""


class MyInt(int):
    def __eq__(self, other):
        """Check if self and other are equal:
        then:
            return true
        else:
            return false
        """
        return int(self) != other

    def __ne__(self, other):
        """
        check if self and other not equal:
        then:
            returns true
        else:
            returns false
        """
        return int(self) == other
