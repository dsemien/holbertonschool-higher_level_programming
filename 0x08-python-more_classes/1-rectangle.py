#!/usr/bin/python3
""" A classy Rectangle module.
"""


class Rectangle:
    """ A class that defines a Rectangle.
    """

    def __init__(self, width=0, height=0):
        """ Initialiation of a Rectangle object.
        Arguments:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.            
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ A function that gets the value of width for Rectangle.
        Returns:
            The value of width.
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ A function that sets the value of width for Rectangle.
        Arguments:
            value (int): Widths set value.
        """
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return(self.__width)

    @property
    def height(self):
        """ A function that gets the value of height for Rectangle.
        Returns:
            The value of height.
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ A function that sets the value of height for Rectangle.
        Arguments:
            value (int): heights set value
        """
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return(self.__height)
