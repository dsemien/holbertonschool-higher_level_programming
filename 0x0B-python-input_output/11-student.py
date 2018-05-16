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

    def to_json(self):
        """ A JSON methon that retrieves a
            dictionary representation of a Student instance
            Returns:
                a dictionary representation of a Student instance
        """
        return self.__dict__
