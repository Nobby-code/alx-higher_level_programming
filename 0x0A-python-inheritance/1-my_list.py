#!/usr/bin/python3
"""List sorting"""


class MyList(list):
    """Class containing the method for sorting"""
    def print_sorted(self):
        """instance of class MyList to sort the list"""
        print(sorted(self))
