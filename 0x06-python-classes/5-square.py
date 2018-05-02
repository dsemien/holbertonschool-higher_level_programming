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

    def area(self):
        """ Calculates area of square
        Return:
            area of square
        """
        return(self.__size ** 2)

    @property  # getter
    def size(self):
        """ Initialization of get private attribute
        Return:
            size of square
        """
        return(self.__size)

    @size.setter  # setter
    def size(self, resize):
        """ Initialization of set __size attribute
        Arguments:
            resize (int): new size of square
        """
        if isinstance(resize, int) is not True:  # check if var is int
            raise TypeError("size must be an integer")
        if resize < 0:
            raise ValueError("size must be >= 0")
        self.__size = resize

    def my_print(self):
        """ prints square to console using #
        """
        if self.__size is 0:
            print()
        else:
            for sqr in range(self.__size):
                print("#" * self.__size)
