#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        row_len = 1
        for j in i:
            if row_len == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            row_len += 1
        print()
