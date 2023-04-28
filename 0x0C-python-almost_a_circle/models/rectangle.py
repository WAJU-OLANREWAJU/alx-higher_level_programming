#!/usr/bin/python3
""" This module is a rectangle class that inherits from Base class """

from models.base import Base

class Rectangle(Base):
    """ A rectangle class that inherits from BAse class
    """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ instantiation of private attributes
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        @property
        def width(self):
            """ funtion to get private instance """
            pass

        @width.setter
        def width(self, value):
            """ setter for private instance """
            pass

        @property
        def height(self):
            pass

        @height.setter
        def height(self, value):
            """ setter for private instance """
            pass

        @property
        def x(self):
            """ funtion to get private instance """
            pass

        @x.setter
        def x(self, value):
            """ setter for private instance """
            pass

        @property
        def y(self):
            """ funtion to get private instance """
            pass

        @y.setter
        def y(self, value):
            """ setter for private instance """
            pass



