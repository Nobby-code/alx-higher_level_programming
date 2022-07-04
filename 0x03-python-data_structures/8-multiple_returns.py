#!/usr/bin/python3

def multiple_returns(sentense):
    if len(sentense) == 0:
        new_tuple = (0, None)
    else:
        first_char = sentense[:1]
        new_tuple = len(sentense), first_char

    return new_tuple
