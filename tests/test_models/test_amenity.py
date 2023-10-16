#!/usr/bin/python3
"""
The Unittest for Amenity
"""
import unittest
from datetime import datetime
from time import sleep
import os
from models import storage
from models.amenity import Amenity


class TestAmenity_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of Amenity class
    """

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amenity = Amenity()
        cls.amenity.name = "Test"

    @classmethod
    def tearDownClass(cls):
        """Tear down unittest"""
        del cls.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """
        Test instantiation of Amenity class
        """
        a1 = Amenity()
        self.assertIsInstance(a1, Amenity)
        self.assertEqual(str(
          type(a1)), "<class 'models.amenity.Amenity'>")
        self.assertTrue(issubclass(type(a1), Amenity))

    def test_instantiation_with_id(self):
        """
        Test instantiation of Amenity class with id
        """
        a1 = Amenity()
        self.assertTrue(hasattr(a1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        a1 = Amenity()
        self.assertEqual(type(a1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        a1 = Amenity()
        a2 = Amenity()
        for inst in [a1, a2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(a1.id, a2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        a1 = Amenity()
        self.assertTrue(hasattr(a1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        a1 = Amenity()
        self.assertIsInstance(a1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        a1 = Amenity()
        self.assertTrue(hasattr(a1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        a1 = Amenity()
        self.assertIsInstance(a1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        a1 = Amenity()
        diff = a1.updated_at - a1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(Amenity().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        a1 = Amenity()
        a1.id = "123456"
        a1.created_at = a1.updated_at = dt
        a1_str = a1.__str__()
        self.assertIn("[Amenity] (123456)", a1_str)
        self.assertIn("'id': '123456'", a1_str)
        self.assertIn("'created_at': " + dt_repr, a1_str)
        self.assertIn("'updated_at': " + dt_repr, a1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        a1 = Amenity()
        string = "[{}] ({}) {}".format(
          "Amenity", a1.id, str(a1.__dict__))
        self.assertEqual(str(a1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        a1 = Amenity()
        string = "[Amenity] ({}) {}".format(
          a1.id, a1.__dict__)
        self.assertEqual(string, str(a1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        a1 = Amenity(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(a1.id, "345")
        self.assertEqual(a1.created_at, dt)
        self.assertEqual(a1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        a1 = Amenity(None)
        self.assertNotIn(None, a1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(Amenity(), storage.all().values())


class TestAmenity_save_method(unittest.TestCase):
    """
    Unittest for Amenity save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        a1 = Amenity()
        updated_at_1 = a1.updated_at
        a1.save()
        updated_at_2 = a1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        a1 = Amenity()
        sleep(0.1)
        updated_at_1 = a1.updated_at
        a1.save()
        updated_at_2 = a1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        a1.save()
        self.assertLess(updated_at_2, a1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        a1 = Amenity()
        with self.assertRaises(TypeError):
            a1.save(None)


class TestAmenity_to_dict_method(unittest.TestCase):
    """
    Unittests for Amenity to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        a1 = Amenity()
        dic = a1.to_dict()
        self.assertNotEqual(dic, a1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        a1 = Amenity()
        dic = a1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        a1 = Amenity()
        self.assertTrue(dict, type(a1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        a1 = Amenity()
        self.assertIn("id", a1.to_dict())
        self.assertIn("created_at", a1.to_dict())
        self.assertIn("updated_at", a1.to_dict())
        self.assertIn("__class__", a1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        a1 = Amenity()
        dt = datetime.today()
        a1.id = "123456"
        a1.created_at = a1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'Amenity',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(a1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        a1 = Amenity()
        with self.assertRaises(TypeError):
            a1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        a1 = Amenity()
        a1.name = "Test"
        a1.age = 5
        dic = a1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
