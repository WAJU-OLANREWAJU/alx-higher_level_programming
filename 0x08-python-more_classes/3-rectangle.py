#!/usr/bin/python3
"""This module adds string representation (based on 2-rectangle.py).
"""

class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
    
    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            output = ""
            for _ in range(self.__width):
                for _ in range(self.__height):
                    output += "#"
                output += "\n"
                    
            return output
