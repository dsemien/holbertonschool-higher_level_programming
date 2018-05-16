#!/usr/bin/python3
"""Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class
        Arguments:
            obj (obj): checks instance
            a_class (class): checks instance
        Returns:
            True if object is an instance
            or False if not
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
