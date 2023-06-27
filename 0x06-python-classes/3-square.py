#!/usr/bin/python3
class Square:
    """ Defines a class Square. """

    def __init__(self, size=0):
        """ Instantiate Square class.
        Arguments:
        @size: Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Fine the area of a square.
        Return:
        Power of square size.
        """
        return ((self.__size) ** 2)
