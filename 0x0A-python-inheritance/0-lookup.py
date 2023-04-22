#!/usr/bin/python3

def lookup(obj):
    """
    Checks and returns the list of available objects and methods.
    Args:
        obj: The class to check its objects and methods.
    return:returns the list of available attributes and methods of an object.
    """
    return dir(obj)
