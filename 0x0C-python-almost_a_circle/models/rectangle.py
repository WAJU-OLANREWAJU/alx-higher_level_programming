#!/usr/bin/python3
"""This is a rectangle module"""

from models.base import Base

class Rectangle(Base):
    """This is a subclass of the Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Allows the private attribute 'width' to be accessible"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allows to validate private attribute 'width'"""
        pass

    @property
    def height(self):
        """Allows the private attribute 'height' to be accessible"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allows to validate private attribute 'height'"""
        pass

    @property
    def x(self):
        """Allows the private attribute 'x' to be accessible"""
        return self.__x

    @x.setter
    def x(self, value):
        """Allows to validate private attribute 'x'"""
        pass

    @property
    def y(self):
        """Allows the private attribute 'y' to be accessible"""
        return self.__y

    @width.setter
    def y(self, value):
        """Allows to validate private attribute 'y'"""
        pass




