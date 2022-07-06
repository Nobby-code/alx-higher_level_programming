#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_dict = max(a_dictionary, key=a_dictionary.get)
    else:
        max_dict = None
    return max_dict
