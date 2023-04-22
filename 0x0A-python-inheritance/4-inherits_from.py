#!/usr/bin/python3

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
    return isinstance(obj, a_class)
