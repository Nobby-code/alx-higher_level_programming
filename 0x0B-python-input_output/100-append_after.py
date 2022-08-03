#!/usr/bin/python3
"""Append ater a specific word"""


def append_after(filename="", search_string="", new_string=""):
    """
    def append_after(filename="", search_string="", new_string=""
    Arguments:
        filename - name of the file to operate on
        search_string - The string to search if it exists of filename
        new_string - string to add aftter the found string

    """
    append_text = ""

    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            append_text = append_text + line
            if search_string in line:
                append_text = append_text + new_string

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(append_text)
