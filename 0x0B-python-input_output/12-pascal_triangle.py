#!/usr/bin/python3
""" A module that defines a pascal triangle """


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        List of Lists: A list of lists representing Pascal's Triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle


