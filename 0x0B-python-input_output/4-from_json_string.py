#!/usr/bin/python3
"""This is a From JSON string to Object Module."""


import json

def from_json_string(my_str):
    """This function returns an object (Python data structure) represented by a JSON string.
    Args:
        my_str: object (Python data structure) represented by a JSON string to be returned.
    """
    return json.loads(my_str)
