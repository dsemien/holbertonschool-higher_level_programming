#!/usr/bin/python3
""" Creation of a Class
"""


class Square:
    """ fancy square
    Attributes:
        size (str): size of square
    """
    def __init__(self, size=0):
        """ Initialization of square
        Arguments:
            size (int): size of square
        """
        if isinstance(size, int) is not True:  # check if var is int
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
