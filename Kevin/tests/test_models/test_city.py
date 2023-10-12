#!/usr/bin/env python3
"""
Module to test City Class
"""
import unittest #type: ignore
import uuid
from datetime import datetime
from models import storage
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
     """
     Unittests for City Class
     """
     city = City()
     city.state_id = str(uuid.uuid4())
     city.name = "Test"

     def test_city_is_a_subclass_of_base_model(self):
         """
         Test if City is a subclass of BaseModel
         """
         self.assertTrue(issubclass(self.city.__class__, BaseModel))

     def test_