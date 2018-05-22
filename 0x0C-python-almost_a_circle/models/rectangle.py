#!/usr/bin/python3
"""Rectangle subclass of Base superclass"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle subclass of superclass BaseGeometry
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialiation of a Rectangle object.
        Arguments:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
            x (int): x axis
            y (int): y axis
            id (int): identity of an object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """A function that gets the value of width for Rectangle.
        Returns:
            The value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """A function that sets the value of width for Rectangle.
        Arguments:
            value (int): Width set value.
        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """A function that gets the value of height for Rectangle.
        Returns:
            The value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """A function that sets the value of height for Rectangle.
        Arguments:
            value (int): heights set value
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ A function that gets the value of x for Rectangle.
        Returns:
            The value of x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """A function that sets the value of x for Rectangle.
        Arguments:
            value (int): x set value
        """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """ A function that gets the value of y for Rectangle.
        Returns:
            The value of y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ A function that sets the value of y for Rectangle.
        Arguments:
            value (int): y set value
        """
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ area method of Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ display method of Rectangle
        """
        print('\n' * self.y, end='')
        for space in range(self.height):
            print(' ' * self.x, end='')
            for symbol in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        """ Prints a string representation of Rectangle.
        """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def to_dictionary(self):
        """ A dictionary representation of a Rectangle
            Returns:
                dictionary representation of a Rectangle
        """
        arg_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            }
        return arg_dict

    def update(self, *args, **kwargs):
        """ An Update method of Rectangle
        Arguments:
            args (list): sends a non-keyworded variable
            length argument list to the function
            kwargs (dict): sends a keyworded variable
            length argument to the function
        """
        arg_list = ['id', 'width', 'height', 'x', 'y']
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for index, argument in enumerate(args):
            setattr(self, arg_list[index], argument)
