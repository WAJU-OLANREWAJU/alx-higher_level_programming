#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """ My base class """

    def area(self):
        """ This method has nothing defined so it raises an exception where there is an attempt to be invoked """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
         """
         An integer validation for value.
         Args:
             self: placeholder for instantiation
             name: The first param and it is always a string.
             value: The second param and below is its validation.
         Returns:
             raises an exception error
         """
         if not isinstance(value, int):
             raise TypeError("{} must be an integer".format(name))
         elif value <= 0:
             raise ValueError("{} must be greater than 0".format(name))

