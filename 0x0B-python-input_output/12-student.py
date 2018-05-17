#!/usr/bin/python3
"""A Student Class
"""


class Student:
    """A Student superclass
    """
    def __init__(self, first_name, last_name, age):
        """inilization of Student
         Arguments:
            first_name (str): first name of Student.
            last_name (str): last name of Student.
            age (int): age of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A JSON methon that retrieves a
            dictionary representation of a Student instance
        Arguments (str):
            string of attributes
        Returns:
            a dictionary representation of a Student instance
        """
        dictionary = {}
        if attrs is None:
            return self.__dict__
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary
