#!/usr/bin/python3
"""Matrix calculations"""

def matrix_divided(matrix, div):
    """
    function matrix_divided():
        takes two arguments: matrix and div
        matrix -list of lists of type integer or float
        div - number to divide each element
        
        Raises:
            TypeError if matrix not a list of lists
            ZeroDivisionError if div is zero
            TypeError if div is not int or float
        return new_list
    """
    new_matrix = []

    length = len(matrix[0])

    if type(matrix) is not list:
        raise TypeError("matrix must be (list of lists) of integers/floats")
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
 
    for inner_matrix in matrix:
        if type(inner_matrix) is not list or inner_matrix == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if any(type(element) not in [int, float] for element in inner_matrix):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(inner_matrix) != length:
            raise TypeError("each row of the matrix must have the same size")
        new_matrix.append(list(map(lambda element: round(element / div, 2), inner_matrix)))
    return new_matrix
