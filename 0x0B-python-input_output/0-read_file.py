#!/usr/bin/python3
"""Read file Module"""

def read_file(filename=""):
    """Read file function

    Args:
        filename: file to read
    Returns:
        prints to stdout
    """
    with open(filename, encoding='utf-8') as f:
        read = f.read()
        print(read)
