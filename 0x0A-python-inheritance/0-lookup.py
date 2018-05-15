#!/usr/bin/python3
""" a look up method
"""


def lookup(obj):
    """ a function that returns the list of available attributes
    and methods of an object
        Arguments:
            obj (obj): object to lookup.
        Returns:
             list of available attributes and methods of an object
        """
    return dir(obj)
