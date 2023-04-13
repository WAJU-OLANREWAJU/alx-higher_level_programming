#!/usr/bin/python3

class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
      '''  else:
            if isinstance(type(self).print_symbol, list):
                symbol = type(self).print_instance[0] '''
        else:
            symbol = str(type(self).print_symbol)
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += symbol
            result += "\n"
        return result

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

