#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        first = my_list[0]
        for value in my_list:
            if value > first:
                first = value
        return first
