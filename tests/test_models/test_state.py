#!/usr/bin/env python3
"""
Module for State Class tests
"""
import unittest #type: ignore
from time import sleep #type: ignore
from datetime import datetime #type: ignore


class TestState_instantiation(unittest.TestCase):
    """
    Unittest for State Class
    """
    def test_instantiation(self):
        """
        Test if State Class is properly initialized
        """
        state = __import__("models.state").state.State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, __import__("models.state").state.State)
        self.assertTrue(
          issubclass(
            type(state), 
            __import__("models.base_model").base_model.BaseModel))
    
    def test_instantiation_without_args(self):
        """
        Test when State Class is without arguments
        """
        state = __import__("models.state").state.State(None)
        self.assertEqual(
          __import__("models.state").state.State, 
          type(__import__("models.state").state.State()))
        self.assertNotIn(None, state.__dict__.values())
        
    def test_instantiation_with_kwargs(self):
        """
        Test when State Class is initialized with kwargs
        """
        date = datetime.today()
        date_iso = date.isoformat()
        state = __import__("models.state").state.State(
          id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_instantiation_two_states(self):
        """
        Test two instances of State Class
        """
        state1 = __import__("models.state").state.State()
        state2 = __import__("models.state").state.State()
        self.assertNotEqual(state1.id, state2.id)
