#!/usr/bin/env python3
"""
Module to test City Class
"""
import unittest #type: ignore
import uuid
from datetime import datetime


class TestCity(unittest.TestCase):
     """
     Unittests for City Class
     """
     city = __import__("models.city").city.City()
     city.state_id = str(uuid.uuid4())
     city.name = "Test"

     def test_city_is_a_subclass_of_base_model(self):
         """
         Test if City is a subclass of BaseModel
         """
         self.assertTrue(issubclass(
           self.city.__class__,
          __import__("models.base_model").base_model.BaseModel))
