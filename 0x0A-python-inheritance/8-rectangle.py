#!/usr/bin/python3
"""This is a rectangle module that inherits from the BaseGeometry.
based on  (7-base_geometry.py).
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Inheits a super class BaseGeometry"""

    def __init__(self, width, height):
        """consructor for the sub class Rectangle"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
