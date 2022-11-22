#!/usr/bin/python3
"""The ``file_storag`` module

This module contains the ``FileStorage``
"""
import json


class FileStorage():
    """This class serializes instances to a JSON file and
        deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary ``__objects``
        """
        return self.__objects

    def new(self, obj):
        """Sets in ``__objects`` the ``obj`` with key ``<obj class name>.id``
        """
        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = str(obj)

    def save(self):
        """Serializes ``__objects to the JSON file
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
            to_json_string = json.dumps(self.__objects)
            a_file.write(to_json_string)

    def reload(self):
        """Deserializes the JSON file to ``__objects`` (only if the JSON file
            (`__file_path`) exits; otherwise, do nothing. If the file doesn't
            exist, no exception should raised
        """
        try:
            a_file = open(self.__file_path, mode='r', encoding='utf-8')
        except FileNotFoundError:
            pass
        else:
            json_string = a_file.read()
            a_file.close()
            FileStorage.__objects = json.loads(json_string)
