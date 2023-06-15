#!/usr/bin/python3
"""Module baserd on (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Inherits from Rectangle Module"""
    def __init__(self, size):
        """method constructor to instantiate size"""
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__size = size



