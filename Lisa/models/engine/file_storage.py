#!/usr/bin/ python3
"""
Module that serializes instances to a JSON file
and deserializes JSON file to instances
"""

import json
import os


class FileStorage:
  """
  File Storage Class
  """
  __file_path = "file.json"
  __objects = {}
  
  def all(self):
    """
    Returns all objects
    """
    return FileStorage.__objects

  def new(self, obj):
    """
    Adds a new object
    
    Args:
    obj: The object to be added
    """
    class_name = obj.__class__.__name__
    key = "{}.{}".format(class_name, obj.id)
    FileStorage.__objects[key] = obj

  def save(self):
    """
    Serializes instances to JSON file
    """
    serialize_obj = {serialized = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}}
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
