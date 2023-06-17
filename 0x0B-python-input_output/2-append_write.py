#!/usr/bin/python3
"""Append to a File Module"""

def append_write(filename="", text=""):
    """This function Appends to a file.
    Args:
        filename: file to write to.
        text: text to write to a file.
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)


