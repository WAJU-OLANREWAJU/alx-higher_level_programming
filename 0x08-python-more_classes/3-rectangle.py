#!/usr/bin/python3

class Rectangle:

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return int(self.__width) * int(self.__height)

    def perimeter(self):
        n_perimeter = 2 * int(self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            n_perimeter = 0
            return n_perimeter
        else:
            return n_perimeter
    
    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
        else:
            result = ""
            for i in range(self.__height):
                for j in range(self.__width):
                    result += "#"
                result += "\n"
            return result
