#!/usr/bin/env python3
"""
Module for tests of Console
"""
import os   # type: ignore
from console import HBNBCommand
from datetime import datetime
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
        Test if help works
        """
        h = "Exit the command interpreter.\n        Usage: quit"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())


class TestHBNBCommand_show(unittest.TestCase):
    """
    Unittests for Show command
    """
    def test_instantiation_show(self):
        """
        Test if show works
        """
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review"))
            self.assertEqual(correct, output.getvalue().strip())

    # def test_instantiation_show_with_invalid_class(self):
    #  """
    #  Test if show instantiates invalid object
    #  """
    #  with patch("sys.stdout", new=StringIO()) as output:
    #      self.assertFalse(HBNBCommand().onecmd("show TestModel"))
    #      self.assertEqual(
    #    "** class doesn't exist **", output.getvalue().strip())

    def test_instantiation_show_with_invalid_id(self):
        """
        Test if show handles invalid id
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show BaseModel 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show User 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show City 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show State 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Review 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Place 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show Amenity 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())


class TestHBNBCommand_destroy(unittest.TestCase):
    """
    Unittests for Destroy command
    """
    def test_instantiation_destroy_no_object(self):
        """
        Test if destroy works
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(
                    "** class name missing **", output.getvalue().strip())

    # def test_instantiation_destroy_with_invalid_class(self):
    #  """
    #  Test if destroy handles invalid class
    #  """
    #  with patch("sys.stdout", new=StringIO()) as output:
    #    self.assertFalse(HBNBCommand().onecmd("destroy TestModel"))
    #    self.assertEqual(
    #      "** class doesn't exist **", output.getvalue().strip())

    def test_instantiation_destroy_with_no_id(self):
        """
        Test if destroy handles no id
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip()
            )
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(
                    "** instance id missing **", output.getvalue().strip())

    def test_instantiation_destroy_with_invalid_id(self):
        """
        Test if destroy handles invalid id
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
            self.assertEqual(
                    "** no instance found **", output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
