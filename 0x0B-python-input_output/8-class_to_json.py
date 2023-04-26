#!/usr/bin/python3

""" This module Write a function that returns the dictionary description with simple data structure 
(list, dictionary, string, integer and boolean) for JSON serialization of an object. """

def class_to_json(obj):
    """
    Serialize an object to a dictionary representation with simple data structures
    Args:
        obj: The object to be serialized
    Returns:
        dict: The dictionary representation of the object
    """
    return obj.__dict__
