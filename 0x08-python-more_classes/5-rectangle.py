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
        self.__width = value

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
        self.__height = value

    def area(self):
        """Calc the area of Rectangle.
        Returns:
            area of Rectangle.
        """
        return(self.__width * self.height)

    def perimeter(self):
        """Calc the perimeter of Rectangle.
        Returns:
            perimeter of Rectangle.
        """
        if self.width is 0 or self.height is 0:
            return(0)
        return((self.width + self.height) * 2)

    def __str__(self):
        """ Prints a string representation of Rectangle.
        """
        if self.width is 0 or self.height is 0:
            return("")
        else:
            return("\n".join(("#" * self.width)for element in range(self.height)))
    
    def __repr__(self):
        """compute the “official” string representation of an object.
        Returns:
            string representation of an object. 
        """
        return("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """a destructor of rectangle.
        """
        print("Bye rectangle…")
