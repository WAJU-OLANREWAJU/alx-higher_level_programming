#!/usr/bin/python3
""" A module  writes an Object to a text file, using a JSON representation. """

import json
""" import a sys lib """

def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as file:
        sv_to_jsn_file = json.dump(my_obj, file, ensure_ascii=false)
        return sv_to_jsn_file
