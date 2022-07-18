#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Function to print a list of only integers in a list
    catches out of range exception
    """
    count = 0

    for element in range(0, x):
        try:
            print("{:d}".format(my_list[element]), end='')
            count = count + 1
        except (TypeError, ValueError):
            pass
    print()
    return (count)
