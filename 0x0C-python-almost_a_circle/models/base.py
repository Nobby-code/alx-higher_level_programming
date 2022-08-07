#!/usr/bin/python3

"""
Base class. It is the base of all other classes in the project
"""
import json
import os


class Base:
    """
    class Base:
        has a class variable __nb_objects = 0
        increases __nb_objects if id is not None
        else:
            assigns self.id to id
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor function to initialize the id
        """
        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        def to_json_string(list_dictionaries):
            A function that returns the json representation of
            a list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        return json.dumps(list_dictionaries)

    @staticmethod
    def save_to_file(cls, list_objs):
        """
        def save_to_file(cls, list_objs):
            Function that writes json formatted string to a file
        """

        my_file = cls.__name__ + ".json"
        my_list = []

        if list_objs is None:
            return []

        for element in list_objs:
            my_list.append(element.to_dictionary())

        to_json = cls.to_json_string(my_list)

        with open(my_file, "w") as f:
            f.write(to_json)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        my_file = cls.__name__ + ".json"
        my_list = []

        if list_objs is not None:
            for element in list_objs:
                my_list.append(element.to_dictionary())

        json_string = cls.to_json_string(my_list)

        with open(my_file, mode='w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        converting from json string format to dictionary
        """
        if json_string is None and len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """crating instance of a dictionary with already set attrinutes"""
        if cls.__name__ == "Rectangle":
            temp = cls(1, 2)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """loading instance file """
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json", "r") as file:
            stuff = cls.from_json_string(file.read())
        return [cls.create(**index) for index in stuff]
