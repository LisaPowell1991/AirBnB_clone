#!/usr/bin/env python3
"""
A module that defines all common attributes/methods
"""
import uuid
from datetime import datetime
import models


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
        pass

    def to_dict(self):
        """
        Returns a dictionary of the object's attributes
        """
        pass

    def __str__(self):
        """
        Prints the object's attributes
        """
        pass
