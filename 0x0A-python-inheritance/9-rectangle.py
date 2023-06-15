#!/usr/bin/python3
"""This module is  (based on 6-base_geometry.py)"""

class BaseGeometry:
    """An empty class"""

    def area(self):
        """A public instance method

        Raises:
            Exception.
        """ 
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that validates value"""

        if not isinstance(value, int):
            #raises TypeError if condition not met
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            #raises ValueError if condition not met
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Inheits a super class BaseGeometry"""

    def __init__(self, width, height):
        """consructor for the sub class Rectangle"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[{}] {}/{}".format(__class__.__name__, self.__width, self.__height)
