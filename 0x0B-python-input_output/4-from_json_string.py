#!/usr/bin/python3
""" This module Write a function that returns an object (Python data structure) represented by a JSON string."""

import json
""" This imports sys lib """

def from_json_string(my_str):
    """ a function that returns an object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
