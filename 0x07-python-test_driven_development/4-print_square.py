#!/usr/bin/python3
"""
    This module writes a fuction that prints a square with the character '#'.
"""

def print_square(size):
    """ This function takes only an 'int' as a positional argument for 'size', which in turn prints an '#' character square with.

    Args:
        size (int): The only parameter.

    Returns:
        prints a square with the character '#'.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()

