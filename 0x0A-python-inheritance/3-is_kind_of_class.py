#!/usr/bin/python3
"""This module checks if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
"""

def is_kind_of_class(obj, a_class):
    """Function that checks what is stated in the module

    Args:
        obj: The object to be checked
        a_class: The class to check, could be super or sub class.

    Returns:
        True: if the object is an instance of the specified class.
        False: if the object is an instance of a class that inherited from, the specified class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
