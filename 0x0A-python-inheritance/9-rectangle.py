#!/usr/bin/python3
"""An BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
