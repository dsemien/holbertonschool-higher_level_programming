#!/usr/bin/python3
"""An BaseGeometry class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A classy Square
    """

    def __init__(self, size):
        """inilization of Square
         Arguments:
            size (int): size of Square.
        """
        super().integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
