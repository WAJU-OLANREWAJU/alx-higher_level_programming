#!/usr/bin/python3
""" This module writes a function that returns the JSON repr of an object"""
import json
""" This import sys lib """

def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string).
    """
    return json.dumps(my_obj)


