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
            return self.__width

        @width.setter
        def width(self, value):
            """ setter for private instance """
            if type(value) != int:
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
            if type(value) != int:
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
            if type(value) != int:
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
            if type(value) != int:
                raise TypeError("x must be an integer")
            elif value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value


    def area(self):
        """ This returns the area of a rectangle
        """
        return (self.__height * self.__width)

    
    def display(self):
        """ This prints to the stdout a rectangle with "#" character
        """
        for i in range(self.__width):
            for j in range(self.__height):
                print("#", end="")
        for i in range(self.__X):
            for j in range(self.__y):
                print("$", end="")
            print()


    def __str__(self):
        """ This returns __str__ of the output
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """ This method assigns an argument to each at a specified position
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.__width = arg
                elif a == 2:
                    self.__height = arg
                elif a == 3:
                    self.__x = arg
                elif a == 4:
                    self.__y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.__width = v
                elif k == "height":
                    self.__height = v
                elif k == "x":
                    self.__x = v
                elif k == "y":
                    self.__y = v


