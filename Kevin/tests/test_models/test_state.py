#!/usr/bin/env python3
"""
Module for State Class tests
"""
import unittest #type: ignore
from time import sleep #type: ignore
from datetime import datetime #type: ignore
from models import storage #type: ignore
from models.state import State
from models.base_model import BaseModel


class TestState_instantiation(unittest.TestCase):
    """
    Unittest for State Class
    """
    def test_instantiation(self):
        """
        Test if State Class is properly initialized
        """
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))
    
    def test_instantiation_without_args(self):
        """
        Test when State Class is without arguments
        """
        state = State(None)
        self.assertEqual(State, type(State()))
        self.assertNotIn(None, state.__dict__.values())
        
    def test_instantiation_with_kwargs(self):
        """
        Test when State Class is initialized with kwargs
        """
        date = datetime.today()
        date_iso = dt.isoformat()
        state = State(id="123", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "123")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_instantiation_two_states(self):
        """
        Test two instances of State Class
        """
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)