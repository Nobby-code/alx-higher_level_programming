#!/usr/bin/python3

"""
Student module
"""


class Student:
    """Constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieving dictionary representation of student instance
        """
        my_dict = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if i in self.__dict__:
                my_dict[i] = self.__dict__[i]
        return my_dict
