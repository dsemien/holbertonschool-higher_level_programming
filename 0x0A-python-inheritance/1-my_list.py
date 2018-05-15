#!/usr/bin/python3
""" MyList class
"""


class MyList(list):
    """A class subclass of list super class
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
