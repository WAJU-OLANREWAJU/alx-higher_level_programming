#!/usr/bin/python3
""" A module that writes to a text file """

def write_file(filename="", text=""):
    """ This function writes a string to a text file (UTF8)
    and returns the number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_char = file.write(text)
        return nb_char
