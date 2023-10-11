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
    serialize_obj = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
    with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
      file.write(json.dumps(serialize_obj))

  def reload(self):
    """
        Deserializes JSON file to instances
        """
    try:
      with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        for key, obj_data in data.items():
          class_name, obj_id = key.split(".")
          obj_class = models.classes[class_name]
          obj = obj_class(**obj_id)
          self.new(obj)
    except FileNotFoundError:
      pass
