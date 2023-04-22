#!/usr/bin/python3
"""this module defines a class MyInt that inherits from int..."""


class MyInt(int):
    """ Defines a subclass; MyInt, that inherits a builtin class; int.
    """
    def __eq__(self, other):
        """ this defines a new behavior for the __eq__ magic method """
        return int(self) != int(other)

    def __ne__(self, other):
        """ this defines a new behavior for the __ne__ magic method """
        return int(self) == int(other)
