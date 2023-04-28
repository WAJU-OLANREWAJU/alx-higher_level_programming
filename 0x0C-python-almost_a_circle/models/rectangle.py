#!/usr/bin/python3
""" This module is a rectangle class that inherits from Base class """

from models.base import Base

class Rectangle(Base):
    """ A rectangle class that inherits from BAse class
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ instantiation of private attributes
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ funtion to get private instance """
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for private instance """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            """ setter for private instance """
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """ funtion to get private instance """
            return self.__x

        @x.setter
        def x(self, value):
            """ setter for private instance """
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            elif value < 0:
                raise ValueError("x must be >= 0")
            self.__height = value

        @property
        def y(self):
            """ funtion to get private instance """
            return self.__y

        @y.setter
        def y(self, value):
            """ setter for private instance """
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value





