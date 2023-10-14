#!/usr/bin/ python3
"""
Module that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import datetime
import json
import os


class FileStorage:
    """
    File Storage Class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return all objects in storage or a specific class."""
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object

        Args:
        obj: The object to be added
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ Serializes instances to JSON file """
        serialized_objects =
        {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ Deserializes JSON file to instances """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = FileStorage.class_dict[class_name](**obj_dict)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
