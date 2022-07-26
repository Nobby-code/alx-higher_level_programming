#!/usr/bin/python3

""" Method to print first_name and last_name """


def say_my_name(first_name, last_name=""):
    """
    def say_my_name(first_name, last_name=""):
        The arguments must be of type str
        If the arguments are not str:
            raise TypeError
        Return:
            A printed first_name and last_name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
