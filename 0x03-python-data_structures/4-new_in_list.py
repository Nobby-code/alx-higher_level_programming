#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_len = len(my_list) - 1
    if idx < 0 or idx > list_len:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
