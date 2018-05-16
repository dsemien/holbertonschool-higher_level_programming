#!/usr/bin/python3
"""An BaseGeometry class
"""


class BaseGeometry:
    """ A BaseGeometry class
    """
    def area(self):
        """Area method
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ value  validates method
            Arguments:
                name (str): a string
                value (int): int value
        """
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))

class Rectangle(BaseGeometry):
    """A Rectangle subclass of superclass BaseGeometry
    """
    def __init__(self, width, height):
        """inilization of Rectanlge
         Arguments:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height