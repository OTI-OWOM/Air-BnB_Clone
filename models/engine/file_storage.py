#!/usr/bin/python3
"""This module Defines the file storage class"""
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """Defines how objects are stored and retrieved from a json file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all stored objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary
        Uses the format: <class name>.<object id> as the key"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file
        converts objects to their dictionary representation"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes JSON file to __objects
        Recreates objects from their dictionary representation"""

        classes = {
                'Amenity': Amenity,
                'BaseModel': BaseModel,
                'City': City,
                'Place': Place,
                'Review': Review,
                'State': State,
                'User': User
        }

        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    obj_dict = json.load(f)

                    for key, value in obj_dict.items():
                        class_name = value["__class__"]
                        if class_name in classes:
                            self.__objects[key] = classes[class_name](**value)
            except Exception:
                pass
