#!/usr/bin/python3
"""The ``file_storag`` module

This module contains the ``FileStorage``
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
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
        if obj:
            FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """Serializes ``__objects to the JSON file
        """
        dict_obj = {}
        for key, obj in FileStorage.__objects.items():
            dict_obj[key] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as a_file:
            to_json_string = json.dumps(dict_obj)
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
            for key, obj in json.loads(json_string).items():
                obj = eval(obj['__class__'])(**obj)
                FileStorage.__objects[key] = obj
