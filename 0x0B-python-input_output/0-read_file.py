#!/usr/bin/python3
""" This module reads a text file """

def read_file(filename=""):
    """ A function definition that reads a text file and prints to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end'=')
