#!/usr/bin/python3
""" Library providing a declaration of a class 'Square'
"""


class Square():
    """ Specification of a 'Square'
    """
    def __init__(self, size=0):
        """ Instantiate a 'Square'
        """
        if not isinstance(size, int):
            raise TypeError("size ust be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
