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
        h = "Quit command"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

class TestHBNBCommand_create(unittest.TestCase):
    """
    Unittests for Create command
    """
    def test_instantiation_create(self):
      """
      Test if create instantiates objects
      """
      storage = __import__("models.engine.file_storage").FileStorage()
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "BaseModel.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create User"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "User.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create State"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "State.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "City.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "Amenity.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create Place"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "Place.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create Review"))
        self.assertLess(0, len(output.getvalue().strip()))
        testKey = "Review.{}".format(output.getvalue().strip())
        self.assertIn(testKey, storage.all().keys())

    def test_instantiation_create_with_missing_class(self):
      """
      Test if create instantiates objects with missing class
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create"))
        self.assertLess(0, len(output.getvalue().strip()))
        self.assertIn(
          "** class name missing **", output.getvalue().strip())

    def test_instantiation_create_with_invalid_class(self):
      """
      Test if create instantiates invalid object
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create TestModel"))
        self.assertLess(0, len(output.getvalue().strip()))
        self.assertIn(
          "** class doesn't exist **", output.getvalue().strip())

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

    def test_instantiation_show_with_invalid_class(self):
      """
      Test if show instantiates invalid object
      """
      with patch("sys.stdout", new=StringIO()) as output:
          self.assertFalse(HBNBCommand().onecmd("show TestModel"))
          self.assertEqual(
        "** class doesn't exist **", output.getvalue().strip())

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

    def test_instantiation_destroy_with_invalid_class(self):
      """
      Test if destroy handles invalid class
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy TestModel"))
        self.assertEqual(
          "** class doesn't exist **", output.getvalue().strip())

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
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy User 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy City 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy State 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy Review 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy Place 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout" , new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("destroy Amenity 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())

class TestHBNBCommand_all(unittest.TestCase):
    """
    Test if all handles all commands
    """
    def test_instantiation_all_with_invalid_class(self):
       """
       Test if all handles invalid class
       """
       with patch("sys.stdout", new=StringIO()) as output:
         self.assertFalse(HBNBCommand().onecmd("all TestModel"))
         self.assertEqual(
           "** class doesn't exist **", output.getvalue().strip())

    def test_instantiation_all(self):
      """
      Test if all handles all commands
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertFalse(HBNBCommand().onecmd("create User"))
        self.assertFalse(HBNBCommand().onecmd("create City"))
        self.assertFalse(HBNBCommand().onecmd("create State"))
        self.assertFalse(HBNBCommand().onecmd("create Review"))
        self.assertFalse(HBNBCommand().onecmd("create Place"))
        self.assertFalse(HBNBCommand().onecmd("create Amenity"))
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("all"))
        self.assertIn("BaseModel", output.getvalue().strip())
        self.assertIn("User", output.getvalue().strip())
        self.assertIn("State", output.getvalue().strip())
        self.assertIn("Place", output.getvalue().strip())
        self.assertIn("City", output.getvalue().strip())
        self.assertIn("Amenity", output.getvalue().strip())
        self.assertIn("Review", output.getvalue().strip())

    def test_instantiation_all_object(self):
      """
      Test if all handles class objects
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        self.assertFalse(HBNBCommand().onecmd("create User"))
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
        self.assertIn("BaseModel", output.getvalue().strip())
        self.assertNotIn("User", output.getvalue().strip())

class TestHBNBCommand_update(unittest.TestCase):
    """
    Unittests for update command
    """
    def test_instantiation_with_invalid_object(self):
      """
      Test if update handles invalid object
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("update TestModel"))
        self.assertEqual(
          "** class doesn't exist **", output.getvalue().strip())

    def test_instantiation_with_no_id(self):
      """
      Test if update handles no id
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("update BaseModel"))
        self.assertEqual(
          "** instance id missing **", output.getvalue().strip())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("update User"))
        self.assertEqual(
          "** instance id missing **", output.getvalue().strip())

    def test_instantiation_with_invalid_id(self):
      """
      Test if update handles invalid id
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("update BaseModel 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("update User 1"))
        self.assertEqual(
          "** no instance found **", output.getvalue().strip())

    def test_instantiation_with_missing_attribute(self):
      """
      Test if update is without attribute
      """
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        testId = output.getvalue().strip()
        testCmd = "update BaseModel {}".format(testId)
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        self.assertEqual(
          "** attribute name missing **", output.getvalue().strip())
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd("create User"))
        testId = output.getvalue().strip()
        testCmd = "update User {}".format(testId)
      with patch("sys.stdout", new=StringIO()) as output:
        self.assertFalse(HBNBCommand().onecmd(testCmd))
        self.assertEqual(
          "** attribute name missing **", output.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
