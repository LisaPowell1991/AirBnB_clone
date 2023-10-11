#!/usr/bin/env python3
"""
Module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json


class FileStorage:
  """
    File Storage Class
    """

  def __init__(self):
    """
        Class constructor
        """
    self.__file_path = "Kevin/file.json"
    self.__objects = {}

  def all(self):
    """
        Returns all objects
        """
    return self.__objects

  def new(self, obj):
    """
        Sets a new object
        """
    class_name = obj.__class__.__name__
    key = "{}.{}".format(class_name, obj.id)
    self.__objects[key] = obj

  def save(self):
    """
        Serializes instances to JSON file
        """
    serialize_obj = {}
    for key, obj in self.__objects.items():
      serialize_obj[key] = obj
    with open(self.__file_path, 'w') as file:
      file.write(json.dumps(serialize_obj))

  def reload(self):
    """
        Deserializes JSON file to instances
        """
    try:
      with open(self.__file_path, 'r') as file:
        data = json.loads(file.read())
        for key, obj_data in data.items:
          class_name, obj_id = key.split(".")
          obj = eval(class_name)(**obj_data)
          self.__objects[key] = obj
    except FileNotFoundError:
      pass
