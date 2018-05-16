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
