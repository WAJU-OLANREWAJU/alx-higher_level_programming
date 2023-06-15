#!/usr/bin/python3
"""In this method list of available attributes and methods of an object are returned.
"""

def lookup(obj):
    """This function returns the list of available attributes and methods of an object."""
    return dir(obj)
