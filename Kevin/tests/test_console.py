#!/usr/bin/env python3
"""
Module for tests of Console
"""
import os   # type: ignore
from console import HBNBCommand
from datetime import datetime
from models import storage
import unittest
import sys
from io import StringIO
import inspect
from unittest.mock import patch


class TestHBNBCommand_prompting(unittest.TestCase):
    """
    Unittests for HBNBCommand prompting
    """
    def test_instantiation(self):
        """
        Test if prompt is instantiated
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_instantiation_empty_line(self):
        """
        Test response to empty line
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """
    Unittest for HBNBCommand exit
    """
    def test_instantiation_quit(self):
        """
        Test if quit is instantiated
        """
        with patch("sys.stdout", new=StringIO()) as output:
          self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_instantiation_EOF(self):
        """
        Test if EOF is instantiated
        """
        with patch("sys.stdout", new=StringIO()) as output:
          self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHBNBCommand_help(unittest.TestCase):
    """
    Unittest for HBNBCommand create
    """
    def test_instantiation_help(self):
        """
        """
        pass


if __name__ == '__main__':
    unittest.main()
