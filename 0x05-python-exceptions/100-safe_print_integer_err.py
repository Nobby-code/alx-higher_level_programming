#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """
    printing exception o stderr
    
    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as v_t_err:
        print("Exception: {}".format(v_t_err), file=sys.stderr)
        return False
    else:
        return True
