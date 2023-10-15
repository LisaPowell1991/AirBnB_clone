#!/usr/bin/python3
""" A module that consists of the BaseModel class. """

import uuid
from datetime import datetime


class BaseModel:
    """
    A class that represents a base model.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel class.

        Args:
        *args: unused.
        **kwargs: Arbitrary keyword arguments.
        """
        from models.engine.file_storage import FileStorage
        if kwargs is not None and kwargs != {}:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                                value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            FileStorage().new(self)

    def save(self):
        """ Updates the updated_at attribute. """
        from models.engine.file_storage import FileStorage
        self.updated_at = datetime.now()
        FileStorage().save()

    def to_dict(self):
        """
        Converts the object to a dictionary.

        Returns:
        dict:Dictionary containing the instance's attributes and values.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['id'] = self.id
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        A string representation of the object.

        Returns:
        str: A string in the format
        "[<class name>] (<self.id>) <self.__dict__>".
        """
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
