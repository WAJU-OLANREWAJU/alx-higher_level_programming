#!/usr/bin/python3
""" This module defines a class base """


class Base:
    """ Base class definition with a class attrribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
