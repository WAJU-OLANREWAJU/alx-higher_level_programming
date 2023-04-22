#!/usr/bin/python3
""" A module that that creates an Object from a “JSON file”. """

import json
""" Imports a sys module """

def load_from_json_file(filename):
    """ A function that creates an Object from a JSON file.
    """
    with open(filename, 'r' encoding="utf-8") as file:
        ld_frm_json_file = json.load(file)
