#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""
class Rectangle:
    """A class named Rectangle"""
    
    def __init__(self, width=0, height=0):
        """Constructor method, defines two private atributes"""
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """allows for retrieval of the private attribute"""
        return self.__width
    
    @width.setter
    def width(self, width):
        """allows for setting of the private attribute"""
        self.__width = width
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')
    
    @property
    def height(self):
        """allows for retrieval of the private attribute"""
        return self.__height
    
    @height.setter
    def height(self, height):
        """allows for retrieval of the private attribute"""
        self.__height = height
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')
