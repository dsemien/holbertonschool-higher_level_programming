#!/usr/bin/python3
"""progaram that says your name!
"""


def say_my_name(first_name, last_name=""):
    """A progaram that says your name!

    Arguments:
        first_name (str): "First Name"
        last_name (str): "Second Name"

    Raises:
        TypeError: if first_name or last_name is not a str
    """
    if isinstance(first_name, str) is not True:
            raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is not True:
            raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
