#!/usr/bin/python3
"""Defines a class Rectangle that inherits from the baseclass, BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
     """ My rectangle clas, inherits from the base class """
     def __init__(self, width, height):
        """
        An instantiation of my Rectangle subclass.
        Args:
            self: placeholder for instantiation.
            width: takes only a positive integer.
            height: takes only a positive integer.
        Returns:
            the integer_validator method defined in the baseclass.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
    
     def area(self):
         """ Returns the area of a rectangle """
         return int(self.__width * self.__height)

     def __str__(self):
         string = "[" + str(self.__class__.__name__) + "]"
         string += str(self.__width) + "/" + str(self.__height)
         return string
