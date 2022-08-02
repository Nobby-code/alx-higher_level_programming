#!/usr/bin/python3
"""Append module"""


def append_write(filename="", text=""):
    """
    This function adds text argument at the end
    of the filename
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        count = f.write(text)
        return count
