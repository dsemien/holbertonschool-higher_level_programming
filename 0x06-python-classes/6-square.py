#!/usr/bin/python3
""" Creation of a Class
"""


class Square:
    """ fancy square
    Attributes:
        size (str): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialization of square
        Arguments:
            size (int): size of square
            position (tuple): position of square
        """
        self.size = size
        self.position = position

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
    def size(self, pos):
        """ Initialization of set __size attribute
        Arguments:
            resize (int): new size of square
        """
        if isinstance(pos, int) is not True:  # check if var is int
            raise TypeError("size must be an integer")
        if pos < 0:
            raise ValueError("size must be >= 0")
        self.__size = pos

    def my_print(self):
        """ prints square to console using #
        """
        if self.size is 0:
            print()
        else:
            vert, horzon = self.position
            for sqace in range(horzon):
                print()
            for sqr in range(self.size):    
                print(" " * vert, end="")
                print("#" * self.size)


    @property  # getter
    def position(self):
        """ Initialization of get private attribute
        Return:
            position of square
        """
        return(self.__position)

    @position.setter  # setter
    def position(self, pos):
        """ Initialization of set __position attribute
        Arguments:
            pos (int): position of square
        """
        vert, horzon = pos
        if isinstance(pos, tuple) is not True:  # check if var is tuple
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(vert, int) is not True or isinstance(horzon, int) is not True:  # check if var is int
            raise TypeError("position must be a tuple of 2 positive integers")
        if vert < 0 or horzon < 0 or len(pos) is not 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = pos
