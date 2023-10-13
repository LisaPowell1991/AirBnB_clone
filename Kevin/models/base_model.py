#!/usr/bin/env python3
"""
A module that defines all common attributes/methods
"""
#type: ignore
import uuid #type: ignore
from datetime import datetime #type: ignore
from . import storage 

class BaseModel:
    """
    A class that defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the class
        """
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = datetime.fromisoformat(
          kwargs.get('created_at')) if 'created_at' in kwargs else datetime.now()
        self.updated_at = datetime.fromisoformat(
          kwargs.get('updated_at')) if 'updated_at' in kwargs else datetime.now()
        if not kwargs:
          storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary of the object's attributes
        """
        class_name = self.__class__.__name__
        return {
          "__class__": class_name,
          "id": self.id,
          "created_at": self.created_at.isoformat(),
          "updated_at": self.updated_at.isoformat()
        }

    def __str__(self):
        """
        Prints the object's attributes
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
