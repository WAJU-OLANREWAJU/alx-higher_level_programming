#!/usr/bin/python3
"""This Module Saves Object to a file"""

import json

def save_to_json_file(my_obj, filename):
    """This writes an object to a file, using a JSON representation.
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
