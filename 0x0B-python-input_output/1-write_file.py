#!/usr/bin/python3
"""module to write file"""


def write_file(filename="", text=""):
    """
    Writes a text file in UTF format and returns the
    number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
