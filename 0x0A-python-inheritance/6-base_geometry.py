#!/usr/bin/python3

class BaseGeometry:
    """ My base class """

    def area(self):
        """ This method has nothing defined so it raises an exception where there is an attempt to be invoked """
        raise Exception("area() is not implemented")
