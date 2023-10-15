#!/usr/bin/python3
"""
The Unittest for Place
"""
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.place import Place


class TestPlace_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of Place class
    """
    def test_instantiation(self):
        """
        Test instantiation of Place class
        """
        p1 = Place()
        self.assertIsInstance(p1, Place)
        self.assertEqual(str(
          type(p1)), "<class 'models.place.Place'>")
        self.assertTrue(issubclass(type(p1), Place))

    def test_instantiation_with_id(self):
        """
        Test instantiation of Place class with id
        """
        p1 = Place()
        self.assertTrue(hasattr(p1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        p1 = Place()
        self.assertEqual(type(p1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        p1 = Place()
        p2 = Place()
        self.assertNotEqual(p1.id, p2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        p1 = Place()
        p2 = Place()
        for inst in [p1, p2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(p1.id, p2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        p1 = Place()
        self.assertTrue(hasattr(p1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        p1 = Place()
        self.assertIsInstance(p1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        p1 = Place()
        self.assertTrue(hasattr(p1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        p1 = Place()
        self.assertIsInstance(p1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        p1 = Place()
        diff = p1.updated_at - p1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(Place().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(Place().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(Place().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        p1 = Place()
        p1.id = "123456"
        p1.created_at = p1.updated_at = dt
        p1_str = p1.__str__()
        self.assertIn("[Place] (123456)", p1_str)
        self.assertIn("'id': '123456'", p1_str)
        self.assertIn("'created_at': " + dt_repr, p1_str)
        self.assertIn("'updated_at': " + dt_repr, p1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        p1 = Place()
        string = "[{}] ({}) {}".format(
          "Place", p1.id, str(p1.__dict__))
        self.assertEqual(str(p1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        p1 = Place()
        string = "[Place] ({}) {}".format(
          p1.id, p1.__dict__)
        self.assertEqual(string, str(p1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        p1 = Place(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(p1.id, "345")
        self.assertEqual(p1.created_at, dt)
        self.assertEqual(p1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        p1 = Place(None)
        self.assertNotIn(None, p1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(Place(), storage.all().values())


class TestPlace_save_method(unittest.TestCase):
    """
    Unittest for Place save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        p1 = Place()
        updated_at_1 = p1.updated_at
        p1.save()
        updated_at_2 = p1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        p1 = Place()
        sleep(0.1)
        updated_at_1 = p1.updated_at
        p1.save()
        updated_at_2 = p1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        p1.save()
        self.assertLess(updated_at_2, p1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        p1 = Place()
        with self.assertRaises(TypeError):
          p1.save(None)


class TestPlace_to_dict_method(unittest.TestCase):
    """
    Unittests for Place to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        p1 = Place()
        dic = p1.to_dict()
        self.assertNotEqual(dic, p1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        p1 = Place()
        dic = p1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        p1 = Place()
        self.assertTrue(dict, type(p1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        p1 = Place()
        self.assertIn("id", p1.to_dict())
        self.assertIn("created_at", p1.to_dict())
        self.assertIn("updated_at", p1.to_dict())
        self.assertIn("__class__", p1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        p1 = Place()
        dt = datetime.today()
        p1.id = "123456"
        p1.created_at = p1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'Place',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(p1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        p1 = Place()
        with self.assertRaises(TypeError):
           p1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        p1 = Place()
        p1.name = "Test"
        p1.age = 5
        dic = p1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
