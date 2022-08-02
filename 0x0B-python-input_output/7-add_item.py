#!/usr/bin/python3
"""
Module to write to and read from json

It adds the arguments to the end of the file
"""
import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
new_list = []

dir_path = os.path

if dir_path.exists(filename):
    new_list = load_from_json_file(filename)

for i in sys.argv[1:]:
    new_list.append(i)

save_to_json_file(new_list, filename)
