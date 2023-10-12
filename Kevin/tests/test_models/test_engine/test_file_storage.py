#!/usr/bin/env python3
"""
Module for testing the FileStorage class.
"""
import unittest #type: ignore
from models.base_model import BaseModel #type: ignore
from models.engine.file_storage import FileStorage #type: ignore
import json #type: ignore
import os #type: ignore


class FileStorageTest(unittest.TestCase):
    """
    Unittests for the FileStorage class.
    """
    storage = FileStorage()
  
    def test_instantiation(self):
        """
        Test instantiation of the FileStorage class.
        """
        self.assertIsInstance(self.storage, FileStorage)

    def test_instantiation_attributes(self):
        """
        Test if attributes of FileStorage are initialised
        """
        self.assertEqual(hasattr(FileStorage, '__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '__objects'), True)

    def test_instantiation_save_method_with_arg(self):
        """
        Test if save method handles multiple arguments
        """
        arg = "save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as context:
            FileStorage.save(self, 100)
        self.assertEqual(str(context.exception), arg)

    def test_instantiation_reload_method(self):
        """
        Test if reload method is properly initialised
        """
        b1 = BaseModel()
        b1.save()
        self.assertEqual(os.path.exists(self.storage.__file_path), True)
        all = self.storage.all()
        FileStorage().__objects = {}
        self.assertNotEqual(
          all, FileStorage().__objects)
        self.storage.reload()
        for key, value in self.storage.all().items():
            self.assertEqual(all[key].to_dict(), value.to_dict())

    def test_instantiation_file(self):
        """
        Test if file is properly initialised
        """
        b1 = BaseModel()
        b1.save()
        self.assertEqual(os.path.exists(self.storage.__file_path), True)
        self.assertEqual(self.storage.all(), self.storage.__objects)

    def test_instantiation_save_method_and_reload_method(self):
        """
        Test if save and reload methods are working properly
        """
        b1 = BaseModel()
        b1.name = "test"
        b1.save()
        b1_dict = b1.to_dict()
        all_obj = self.storage.all()

        key = b1_dict['__class__'] + "." + b1_dict['id']
        self.assertEqual(key in all_obj, True)

    def test_instantiation_update_method(self):
        """
        Test if update method is working properly
        """
        b1 = BaseModel()
        b1.name_1 = "test_1"
        b1.save()
        b1_dict = b1.to_dict()

        create_1 = b1_dict['created_at']
        update_1 = b1_dict['updated_at']

        b1.name_2 = "test_2"
        b1.save()
        b1_dict = b1.to_dict()
      
        create_2 = b1_dict['created_at']
        update_2 = b1_dict['updated_at']

        self.assertEqual(create_1, create_2)
        self.assertNotEqual(update_1, update_2)
        self.assertEqual(b1_dict['name_1'], "test_1")


if __name__ == "__main__":
    unittest.main()
