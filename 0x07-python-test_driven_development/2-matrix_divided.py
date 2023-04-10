#!/usr/bin/python3

'''
This function takes two arguments, the first must be a list of lists and each elements would be divided by the second
'''

def matrix_divided(matrix, div):
    if not isinstance (matrix, list) or not all(isinstance(row, list) for row in matrix) and not isinstance (matrix, (int, float)):
        '''
        Function definition, the function takes two arguments: matrix, which is the input matrix as a list of lists, and div, which is the div
        isor
        as an integer or a float.
        '''

        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    

    ''' Get the number of rows and columns in the matrix '''
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    ''' Check if all rows have the same number of columns '''
    if not all(len(row) == num_cols for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    ''' checks if div is an int or a float '''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    ''' checks if div is 0 '''
    if div == 0:
        raise ZeroDivisionError("division by zero")

    ''' Cases:
    row: this performs the outer loop
    elem: this performs the inner loop
    round: this rounds up divided elements to two decima;l places
    result: returns the result of the division
    '''
    result = [[round (elem / div, 2) for elem in row] for row in matrix]
    return result
