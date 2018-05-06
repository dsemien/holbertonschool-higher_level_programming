#!/usr/bin/python3
"""A progaram that prints a square with the character #.
"""


def print_square(size):
    """ prints square to console using #

        Arguments:
            size (int): Size of square

        Raises:
            TypeError: if size in not an int.
            ValueError: if size is negative or not equal to 0.
    """
    if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
    if size < 0:
            raise ValueError("size must be >= 0")

    if size is 0:
        print()
    else:
        for sqr in range(size):
            print("#" * size)
