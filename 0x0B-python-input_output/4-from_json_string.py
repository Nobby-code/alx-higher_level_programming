#!/usr/bin/python3

"""
Loading json data from a string
"""
import json


def from_json_string(my_str):
    """
    def from_json_string(my_str):
        loads data
        Args: my_str
    """
    return json.loads(my_str)
