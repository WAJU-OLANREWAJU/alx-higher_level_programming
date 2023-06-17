#!/usr/bin/python3
"""This is a To JSON string Module"""


import json

def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string).
    Args:
        my_obj: the JSON representation of an object (string) to be returned.
    """
    return json.dumps(my_obj)
