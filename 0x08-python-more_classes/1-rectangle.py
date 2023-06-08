#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
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
