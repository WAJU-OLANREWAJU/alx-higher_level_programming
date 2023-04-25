#!/usr/bin/python3
""" This module inserts a line of text to a file """


def append_after(filename="", search_string="", new_string=""):
    """ THis function writes a new line of text to a file after a searcgh string
    """
    with open('filename', r+, encoding="utf-8") as file:
        line = readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')

