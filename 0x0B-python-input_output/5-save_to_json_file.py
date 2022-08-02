#!/usr/bin/python3
"""
module to write JSON to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writing JSON data to file
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
