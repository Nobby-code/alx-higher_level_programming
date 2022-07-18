#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0
    try:
        for element in range(0, x):
            print("{}".format(my_list[element]), end='')
            count = count + 1
    except Exception:
        pass
    print()
    return (count)
