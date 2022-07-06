#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = [[col ** 2 for col in row] for row in matrix]
    return square_matrix
