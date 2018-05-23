#!/usr/bin/python3
"""Base class"""
import json


class Base:
    """ A Base class
    Attributes:
        id (int): id int
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization of base
        Arguments:
            id (int): id int
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ A method to return the JSON string
        representation of list_dictionaries
        Returns:
         the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """A method writes the JSON string
        representation of list_objs to a file
        Arguments:
            list_objs (list): a list
        """
        with open("{:s}.json".format(cls.__name__), mode='w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([cls.to_dictionary(item)
                        for item in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ A method that returns the list of the JSON
        string representation json_string
        Arguments:
            json_string: JSON string representation
        Returns:
            JSON string representation
        """
        empty = []
        if json_string is None or len(json_string) == len(empty):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ A method that returns an instance with all attributes already set
        Arguments:
            dictionary (dict): double pointer to a dictionary
        Returns:
            an instance with all attributes already set
        """
        dummyclass = cls(3, 6, 8)
        dummyclass.update(**dictionary)
        return dummyclass

    @classmethod
    def load_from_file(cls):
        """ A method that returns that returns a list of instances
        Returns:
            a list of instances
        """
        with open("{:s}.json".format(cls.__name__)) as f:
            loadjson = cls.from_json_string(f.read())
            instance = []
            for argument in loadjson:
                instance.append(cls.create(**argument))
            return instance
