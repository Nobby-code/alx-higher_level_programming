#!/usr/bin/python3
"""Pascal triangle function"""


def pascal_triangle(n):
    """
    Returning integer representation of pascal triangle
    """
    my_list = []
    if n <= 0:
        return my_list

    pascal_triangle = [[1]]

    for current_row in range(1, n):
        row = [1]
        previous_row = pascal_triangle[current_row - 1]

        for element in range(1, current_row):
            row.append(previous_row[element] + previous_row[element - 1])
        row.append(1)
        pascal_triangle.append(row)
    return pascal_triangle
