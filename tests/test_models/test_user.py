#!/usr/bin/env python3
"""
Module for testing the User model.
"""
import unittest  # type: ignore
import os
from datetime import datetime
from time import sleep
import uuid

class TestUser(unittest.TestCase):
    """
    Class for testing the User model.
    """
    user = __import__("models.user").user.User()
    user.email = "test@example.com"
    user.password = "123456"
    user.first_name = "Test"
    user.last_name = "User"
    
   
    def TestUser_instantiation(self):
        """
        Test User Class intantiation
        """
        self.assertEqual(str(type(self.user)), "<class 'models.user.User'>")
        self.assertIsInstance(self.user, __import__("models.user").user.User)
        self.assertTrue(issubclass(
          type(self.user),__import__("models.base_model").base_model.BaseModel))

    def TestUser_attributes(self):
        """
        Test User Class attributes
        """
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def TestUser_no_args(self):
        """
        Test if User handles no arguments
        """
        self.assertEqual(
          __import__("models.user").user.User, type(
            __import__("models.user").user.User()))
      
    def TestUser_storage(self):
        """
        Test if User Class stores instances
        """
        self.assertIn(
          __import__("models.user").user.User(),
          __import__("models.engine.file_storage").FileStorage().all().values())

    def TestUser_attribute_type(self):
        """
        Test if User Class attributes are of the correct type
        """
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)

    def TestUser_instance_type(self):
        """
        Test if User Class is subclass of BaseModel
        """
        self.assertTrue(issubclass(
          self.user.__class__, 
          __import__("models.base_model").base_model.BaseModel))
        self.assertIsInstance(
          self.user,
          __import__("models.base_model").base_model.BaseModel)
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))

class TestUser_methods(unittest.TestCase):
    """
    Unittests for User methods
    """
    user = __import__("models.user").user.User()
    user.email = "test@example.com"
    user.password = "123456"
    user.first_name = "Test"
    user.last_name = "User"
  
    def TestUser_save_method(self):
      """
      Test if User save method saves instance
      """
      self.user.save()
      self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def TestUser_to_dict_method(self):
      """
      Test if to_dict method exists in User class
      """
      self.assertTrue('to_dict' in dir(self.user))

    def TestUser_to_dict(self):
      """
      """
      dic = self.user.to_dict()
      self.assertEqual(type(dic), dict)
      for attr in self.user.__dict__:
        self.assertTrue(attr in dic)
        self.assertTrue("__class__" in dic)


if __name__ == "__main__":
    unittest.main()
