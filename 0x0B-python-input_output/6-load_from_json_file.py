#!/usr/bin/python3
"""
Loading JSON data from a file
"""
import json


def load_from_json_file(filename):
    """
    Function to load JSON data from a file
    filename is the name of the file
    The function returns a JSON fle
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
