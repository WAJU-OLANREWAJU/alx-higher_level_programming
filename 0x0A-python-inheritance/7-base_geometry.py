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
