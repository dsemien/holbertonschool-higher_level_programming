#!/usr/bin/python3
""" Square subclass of Rectangle subclass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square subclass of subclass Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialiation of a Square object.
        Arguments:
            size (int): Size of Square.
            x (int): x axis
            y (int): y axis
            id (int): identity of an object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Prints a string representation of Rectangle.
        """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ A function that gets the value of size for Square.
        Returns:
            The value of size from width.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ A function that sets the value of size for Square.
        Arguments:
            value (int): size set value of width.
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ A dictionary representation of a Rectangle
            Returns:
                dictionary representation of a Rectangle
        """
        arg_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return arg_dict

    def update(self, *args, **kwargs):
        """ An Update method of Square
        Arguments:
            args (list): sends a non-keyworded variable
            length argument list to the function
            kwargs (dict): sends a keyworded variable
            length argument to the function
        """
        arg_list = ['id', 'size', 'height', 'x', 'y']
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for index, argument in enumerate(args):
            setattr(self, arg_list[index], argument)
