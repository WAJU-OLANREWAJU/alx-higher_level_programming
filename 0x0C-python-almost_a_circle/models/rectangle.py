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
        """ funtion to get private instance """
        def width(self):
            pass
        
        @width.setter
        """ function to set private instance """
        def width(self, value):
            pass

        @property
        """ funtion to get private instance """
        def height(self):
            pass

        @height.setter
        """ function to set private instance """
        def height(self, value):
            pass

        @property
        """ funtion to get private instance """
        def x(self):
            pass

        @x.setter
        """ function to set private instance """
        def x(self, value):
            pass

        @property
        """ funtion to get private instance """
        def y(self):
            pass

        @y.setter
        """ function to set private instance """
        def y(self, value):
            pass



