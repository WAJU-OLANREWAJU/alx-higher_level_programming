#!/usr/bin/python3
""" This module appends to a string at the end of a txt """

def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8) 
    and returns the number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_append_write = file.append(text)
        return nb_append_write
