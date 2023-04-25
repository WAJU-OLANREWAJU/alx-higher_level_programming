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
    serialized_obj = {}
    if isinstance(obj, list):
        serialized_obj = [class_to_json(item) for item in obj]
    elif isinstance(obj, dict):
        serialized_obj = {k: class_to_json(v) for k, v in obj.items()}
    elif isinstance(obj, (str, int, bool)):
        serialized_obj = obj
    return serialized_obj
