#!/usr/bin/python3
"""Write to a File Module"""

def write_file(filename="", text=""):
    """This function writes to a file.
    Args:
        filename: file to write to.
        text: text to write to a file.
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)




    
