#!/usr/bin/python3
"""Pascal triangle function"""

def pascal_triangle(n):
    my_list = []
    if n <= 0:
        return my_list
    for i in range(n):

