#!/usr/bini/python3
"""This module adds string representation (based on 2-rectangle.py).
"""

class Rectangle:
    """A Rectangle class definition"""

    def __init__(self, width=0, height=0):
        """The constructor method.
        
        Args:
            width: The width of the Rectangle.
            height: The height of the Rectangle.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Allows the private attribute 'width' to be accessible"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the private attribute 'width'>
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If Width is not >= 0.
        """
        self.__width = width
        if not isinstance(self.__width, int):
            raise TypeError('width must be an integer')
        if self.__width < 0:
            raise ValueError('width must be >= 0')

    @property
    def height(self):
        """Allows the private attribute 'height' to be accessible"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the private attribute 'height'>
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is not >= 0.
        """
        self.__height = height
        if not isinstance(self.__height, int):
            raise TypeError('height must be an integer')
        if self.__height < 0:
            raise ValueError('height must be >= 0')

    def area(self):
        """Defines the area method.
        
        Returns:
            The rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """Defines the perimeter method.

        Returns:
            Zero if width or height is 0.
            Otherwise, Returns the perimeter of the Rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
