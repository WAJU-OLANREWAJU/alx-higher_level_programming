#!/usr/bin/python3
''' A Square class definition '''

class Square:
    ''' Initializing the class attributes and privatizing size '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        ''' defines a getter to retrieve the private instance attribute '''
        return self.__size

    @size.setter
    def size(self, value):
        '''
    defines the setter to control the input of the private instanc attribute
    args:
        value: modifies the private instance attribute
    checks:
        Typeerror: value must be an integer
        Valueerror: value must < 0
    '''

        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        elif value < 0:
            raise ValueError ("size must be >= 0")
        else:
            self.__size = value
    
    def area(self):
        ''' returns the square area '''
        return int(self.__size) * int(self.__size)

