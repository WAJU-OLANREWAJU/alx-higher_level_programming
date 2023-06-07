#!/usr/bin/python3
"""This module writes a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """Matrix is a list of lists, the function ensures the positional arguments are either list or floats.
    Thereupon, divides the matrix with positional argument passed to div which can be either int or floats but not zero.

    Args:
        matrix (int or float): The first parameter.
        div (int or float): The second parameter.

    Returns:
        The result of each divided element in the matrix rounded to two decimal places.
    """

    first_row = len(matrix[0])
    if not all(all(isinstance(element, (int, float)) for element in row) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix[1:]:
        if len(row) != first_row:
            raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    return new_matrix

