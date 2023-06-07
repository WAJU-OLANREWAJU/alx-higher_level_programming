#!/usr/bin/python3
"""In this Module, text are printed with 2 new lines after each of these characters: ., ? and :
"""

def text_indentation(text):
    """
    Checks and ensures text is a string then performs the operation described under module's section.

    Args:
        text (str): The only parameter

    Returns:
        prints two new lines after each of these characters: ., ? and : encountered.
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    output = ""
    for char in text:
        output += char
        if char in ['.', ':', '?']:
            output = output.strip() + "$\n$\n"
    
    print(output)
