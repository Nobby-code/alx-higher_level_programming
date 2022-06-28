#!/usr/bin/python3
def remove_char_at(str, n):
    """Creaing a copy of a string without the character at position n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n + 1:])
