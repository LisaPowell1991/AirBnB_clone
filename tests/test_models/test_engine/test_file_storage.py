#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""
#type: ignore
from datetime import datetime #type: ignore
import inspect
import json
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """
    Unittest for the FileStorage class
    """
    def test_instantiation(self):
      """
      Test if FileStorage class is instantiated
      """
      storage_cls = __import__(
        "models.engine.file_storage").FileStorage
      storage_obj = __import__(
        "models.engine.file_storage").FileStorage()
      self.assertIsInstance(storage_obj, storage_cls)
      
    def test_all_returns_dict(self):
        """
        Test that all returns the FileStorage.__objects attr
        """
        storage = __import__(
          "models.engine.file_storage").FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertIs(new_dict, storage._FileStorage__objects)

    def classes(self):
      """
      Dictionary of classes
      """
      return {
        "BaseModel": __import__("models.base_model").base_model.BaseModel,
        "User": __import__("models.user").user.User,
        "State": __import__("models.state").state.State,
        "City": __import__("models.city").city.City,
        "Amenity": __import__("models.amenity").amenity.Amenity,
        "Place": __import__("models.place").place.Place,
        "Review": __import__("models.review").review.Review
      }

    def test_new(self):
        """
        Test that new adds an object to the FileStorage.__objects attr
        """
        storage = __import__("models.engine.file_storage").FileStorage()
        save = storage._FileStorage__objects
        storage._FileStorage__objects = {}
        test_dict = {}
        for key, value in self.classes().items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = save

    def test_save(self):
        """
        Test that save properly saves objects to file.json
        """
        b1 = __import__("models.base_model").base_model.BaseModel()
        storage = __import__("models.engine.file_storage").FileStorage()
        b1.full_name = "BaseModel Instance"
        b1.save()
        bm_dict = b1.to_dict()
        all_objs = storage.all()
        key = bm_dict['__class__'] + "." + bm_dict['id']
        self.assertEqual(key in all_objs, True)

    def test_reload(self):
        """
        Test reload method
        """
        __import__(
          "models.base_model").base_model.BaseModel().save()
        storage = __import__(
          "models.engine.file_storage").FileStorage()
        new_dict = storage.all()
        storage.__objects = {}
        self.assertNotEqual(new_dict, storage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
          self.assertEqual(new_dict[key].to_dict(), value.to_dict())


if __name__ == "__main__":
  unittest.main()
        
