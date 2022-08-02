#!/usr/bin/python3
"""
Returning JSON represenation of an object
"""
import json


def to_json_string(my_obj):
    """
    Function to return JSON representation
    of an object
    """
    return json.dumps(my_obj)
