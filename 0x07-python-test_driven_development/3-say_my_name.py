#!/usr/bin/python3
"""
    This module takes first name and last name as arguments, then prints "My name is <first name> <last name>"
"""

def say_my_name(first_name, last_name=""):
    """ This is a function that prints "My name is..." with the arguments passed to it which must be strings.

    Args:
        first_name (str): The first parameter.
        last_name (str, optional): The second parameter. Okays if not passed.

    Returns:
        My name is <first name> <last name>.
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string$')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string$')
    print("My name is {} {}$".format(first_name, last_name))

