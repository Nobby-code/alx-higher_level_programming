#!/usr/bin/python3
"""Reading file"""


def read_file(filename=""):
    """
    def read_file(filename=''):
        function to read file
        Args: filename is the file to read
    The file is empty by default
    """
    with open(filename, encoding='utf-8') as f:
        res = f.read()
        print(res, end="")
