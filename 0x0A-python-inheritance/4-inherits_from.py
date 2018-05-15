#!/usr/bin/python3
"""Only sub class of
"""


def inherits_from(obj, a_class):
    """checks ifif the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
        Arguments:
            obj (obj): checks instance
            a_class (class): checks instance
        Returns:
            True if object is an instance
            or False if not
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
