#!/usr/bin/python3
"""A Rectangle subclass, Squaore."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ My Square class that inherits from Rectangle """
    def __init__(self, size):
        """
        initializing the sqaure attributes.
        """
        self.integer_validator = ("size", size)
        super().__init__(size, size)
        self.__size = size

