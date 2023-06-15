#!/usr/bin/python3
"""This module checks if a given object is an instance of a specified class or not"""

def is_same_class(obj, a_class):
    """The class definition

    Args:
        obj: an object to be checked
        a_class: a class to check from

    Returns:
        True: if an object is an instance of a class.
        False: if an object is not an instance of a class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
