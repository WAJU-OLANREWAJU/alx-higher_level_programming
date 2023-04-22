#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """
    checks  if the object is an instance of a class that inherited (directly or indirectly) from the specified class.
    Args:
        obj(All): The class to be checked if it inherits from another class.
        a-class: The class to check against.
    Returns:
        bool: True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
        otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
