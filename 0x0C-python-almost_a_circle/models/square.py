#!/usr/bin/python3
""" This module writes a square class that inherits from a rectangle base class
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A square class declaration
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ class instantiation inheriting from tthe logic of base clas and size is assigned logics
        / of width and height
        """
        super().__init__(id, x, y, size, size)
        self.__size = size

    def __str__(self):
        """returns the __str__ of the output
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self._Rectangle__x, self._Rectangle__y, self.__size)
