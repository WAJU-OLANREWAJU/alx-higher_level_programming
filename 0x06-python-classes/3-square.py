#!/usr/bin/python3
''' A class that defines a square with exception handling '''

class Square:
    ''' A Square class defined '''
    def __init__(self, size):
        """Initializing this square class
        Args:
            size: represents the size of the square defined
        Raises:
            TypeError: if size is not integer
            ValueError: if size is < zero
        """
    
        if not isinstance(size, int):
                raise TypeError ("size must be an integer")

        if size < 0:
                raise ValueError("size must be >= 0")

        self.__size = size
   # @property
    
   # '''this allows the size attribute to be accesible later in the code '''
   # def size(self):
    #        return self.__size

    def area(self):
        ''' this method returns the area of the square '''
        
        return int(self.__size) * int(self.__size)
