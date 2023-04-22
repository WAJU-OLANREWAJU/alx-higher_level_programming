#!/usr/bin/python3
"""checks if object is an instance of a class
or an inherited class
"""

def is_kind_of_class(obj, a_class):
    """"
    Checks if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj(Any): Object to be checked if its an instance or inheritance of a specified class.
        a_class(Type): The class to be checked against.

    Returns:
        bool: True if it is an instance, and false if otherwise.
    """
    return isinstance(obj, a_class)
