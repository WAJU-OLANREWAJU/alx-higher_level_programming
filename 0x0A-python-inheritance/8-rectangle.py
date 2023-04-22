#!/usr/bin/python3
"""Inheris from baseGeometry"""
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

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
