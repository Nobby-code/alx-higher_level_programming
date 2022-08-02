#!/usr/bin/python3

"""
Student class
"""


class Student:
    """
    Student class with methods
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieving dictionary of student instance
        """
        return self.__dict__
