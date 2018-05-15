#!/usr/bin/python3
""" checks if obj is an instance of a_class
"""


def is_same_class(obj, a_class):
    """ checks if the object is exactly an
    instance of the specified class
        Arguments:
            obj (obj): checks instance
            a_class (class): checks instance
        Returns:
            True if object is exactly an instance
            or False if not
    """
    if type(obj) is a_class:
        return True
    else:
        return False
