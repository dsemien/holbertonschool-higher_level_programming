#!/usr/bin/python3
"""An BaseGeometry class
"""


class BaseGeometry:
    """ A BaseGeometry class
    """

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

    def area(self):
        """Area method
            Return:
                area of an object
        """
        return self.__width * self.__height

    def __str__(self):
        """Prints a string representation of Rectangle
        """
        return('[Rectangle] {:d}/{:d}'.format(self.__width, self.__height))


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

    def __str__(self):
        """Prints a string representation of Square
        """
        return('[Square] {:d}/{:d}'.format(self.__size, self.__size))
