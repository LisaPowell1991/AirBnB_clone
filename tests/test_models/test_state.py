#!/usr/bin/python3
"""
The Unittest for State
"""
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.state import State


class TestState_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of State class
    """
    def test_instantiation(self):
        """
        Test instantiation of State class
        """
        s1 = State()
        self.assertIsInstance(s1, State)
        self.assertEqual(str(
          type(s1)), "<class 'models.state.State'>")
        self.assertTrue(issubclass(type(s1), State))

    def test_instantiation_with_id(self):
        """
        Test instantiation of State class with id
        """
        s1 = State()
        self.assertTrue(hasattr(s1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        s1 = State()
        self.assertEqual(type(s1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        s1 = State()
        s2 = State()
        self.assertNotEqual(s1.id, s2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        s1 = State()
        s2 = State()
        for inst in [s1, s2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(s1.id, s2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        s1 = State()
        self.assertTrue(hasattr(s1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        s1 = State()
        self.assertIsInstance(s1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        s1 = State()
        self.assertTrue(hasattr(s1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        s1 = State()
        self.assertIsInstance(s1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        s1 = State()
        diff = s1.updated_at - s1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(State().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(State().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(State().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        s1 = State()
        s1.id = "123456"
        s1.created_at = s1.updated_at = dt
        s1_str = s1.__str__()
        self.assertIn("[State] (123456)", s1_str)
        self.assertIn("'id': '123456'", s1_str)
        self.assertIn("'created_at': " + dt_repr, s1_str)
        self.assertIn("'updated_at': " + dt_repr, s1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        s1 = State()
        string = "[{}] ({}) {}".format(
          "State", s1.id, str(s1.__dict__))
        self.assertEqual(str(s1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        s1 = State()
        string = "[State] ({}) {}".format(
          s1.id, s1.__dict__)
        self.assertEqual(string, str(s1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        s1 = State(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(s1.id, "345")
        self.assertEqual(s1.created_at, dt)
        self.assertEqual(s1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        s1 = State(None)
        self.assertNotIn(None, s1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(State(), storage.all().values())


class TestState_save_method(unittest.TestCase):
    """
    Unittest for State save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        s1 = State()
        updated_at_1 = s1.updated_at
        s1.save()
        updated_at_2 = s1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        s1 = State()
        sleep(0.1)
        updated_at_1 = s1.updated_at
        s1.save()
        updated_at_2 = s1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        s1.save()
        self.assertLess(updated_at_2, s1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        s1 = State()
        with self.assertRaises(TypeError):
            s1.save(None)


class TestState_to_dict_method(unittest.TestCase):
    """
    Unittests for State to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        s1 = State()
        dic = s1.to_dict()
        self.assertNotEqual(dic, s1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        s1 = State()
        dic = s1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        s1 = State()
        self.assertTrue(dict, type(s1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        s1 = State()
        self.assertIn("id", s1.to_dict())
        self.assertIn("created_at", s1.to_dict())
        self.assertIn("updated_at", s1.to_dict())
        self.assertIn("__class__", s1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        s1 = State()
        dt = datetime.today()
        s1.id = "123456"
        s1.created_at = s1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'State',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(s1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        s1 = State()
        with self.assertRaises(TypeError):
            s1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        s1 = State()
        s1.name = "Test"
        s1.age = 5
        dic = s1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
