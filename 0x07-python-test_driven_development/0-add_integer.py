#!/usr/bin/python3
"""A progaram that adds two intergers
"""


def add_integer(a, b=98):
    """adds two intergers

    Arguments:
        a (int): 1st interger
        b (int) (default 98): 2nd interger

    Returns: 
        int: sum of a + b

    Raises:
        TypeError: if a or b is not an int
    """

    if isinstance(a, (int, float)) is not True:
            raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is not True:
            raise TypeError("b must be an integer")
    return(int(a) + int(b))
