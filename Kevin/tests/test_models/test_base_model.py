#!/usr/bin/env python3
"""
The Unittest for BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of BaseModel class
    """
    def test_instantiation(self):
        """
        Test instantiation of BaseModel class
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(str(type(b1)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(b1), BaseModel))

    def test_instantiation_with_id(self):
        """
        """
        pass

    def test_instantiation_id_type(self):
        """
        """
        pass

    def test_distinct_ids(self):
        """
        """
        pass

    def test_instantiation_uuid(self):
        """
        """
        pass

    def test_instantiation_created_at(self):
        """
        """
        pass

    def test_instantiation_created_at_type(self):
        """
        """
        pass

    def test_instantiation_updated_at(self):
        """
        """
        pass

    def test_instantiation_updated_at_type(self):
        """
        """
        pass

    def test_instantiation_datetime(self):
        """
        """
        pass

    def test_instantiation_id_public(self):
        """
        """
        pass

    def test_instantiation_created_at_public(self):
        """
        """
        pass

    def test_instantiation_updated_at_public(self):
        """
        """
        pass

    def test_instantiation_str_method(self):
        """
        """
        pass

    def test_instantantiation_with_args_kwargs(self):
        """
        """
        pass

    def test_instantiation_without_kwargs(self):
        """
        """
        pass

    def test_instantiation_without_args(self):
        """
        """
        pass
