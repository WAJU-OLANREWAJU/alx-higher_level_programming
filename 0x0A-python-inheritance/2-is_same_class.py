#!/usr/bin/python3

def is_same_class(obj, a_class):
    """
    checks if an object is an instance of a particular class.

    Args:
        obj (Any):  The object to be checked.
        a_class (Type): The class to check against.

    Returns:
        bool: True if the object checked is an instance, false if otherwise
    """
    return isinstance(obj, a_class)
