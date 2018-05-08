#!/usr/bin/python3
""" A classy Rectangle module.
"""


class Rectangle:
    """ A class that defines a Rectangle.
    Attributes:
        number_of_instances (int): total count of Rectangle instances
        print_symbol ():
    """
    number_of_instances = 0
    print_symbol = ("#")

    def __init__(self, width=0, height=0):
        """ Initialiation of a Rectangle object.
        Arguments:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        tmp = self.print_symbol
        tmp2 = self.width
        if self.width is 0 or self.height is 0:
            return("")
        else:
            return("\n".join((str(tmp) * tmp2)for e in range(self.height)))

    def __repr__(self):
        """compute the “official” string representation of an object.
        Returns:
            string representation of an object.
        """
        return("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """a destructor of rectangle.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle…")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area
        Arguments:
            rect_1 (obj): 1st Rectangle
            rect_2 (obj): 2nd Rectangle
        Returns:
         biggest rectangle or rect_1 if == to rect_2.
         """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area is rect_2.area:
            return(rect_1)
        else:
            return(rect_2)

    @classmethod
    def square(cls, size=0):
        """ returns a new Rectangle instance with width == height == size
        Arguments:
            size (int): size of rectangle instance.
        Returns:
            size of rectangle instance.
         """
        cls.number_of_instances += 1
        return(cls(size, size))    
