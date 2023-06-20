#!/usr/bin/python3
"""This is a base Module that defines a superclass"""

class Base:
    """A class named Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

