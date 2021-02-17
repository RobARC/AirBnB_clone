#!/usr/bin/pyhton3
"""module engine file_storage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """class serializes and des instances to a JSON file"""

    __file_path = 'file.json'

    __objects = {}

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj with the key <obj class name>.id in __objects"""
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        mydict = {}
        for key, value in FileStorage.__objects.items():
            mydict[key] = value.to_dict()
        with open(fname, 'w') as f:
            json.dump(mydict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        if os.path.exists(self.__file_path) is True:
            with open(self.__file_path, 'r') as f:
                json_objs = json.load(f)
                for key, value in json_objs.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
