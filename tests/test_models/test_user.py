#!/usr/bin/python3
"""
The Unittest for User
"""
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.user import User


class TestUser_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of User class
    """
    def test_instantiation(self):
        """
        Test instantiation of User class
        """
        u1 = User()
        self.assertIsInstance(u1, User)
        self.assertEqual(str(
          type(u1)), "<class 'models.user.User'>")
        self.assertTrue(issubclass(type(u1), User))

    def test_instantiation_with_id(self):
        """
        Test instantiation of User class with id
        """
        u1 = User()
        self.assertTrue(hasattr(u1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        u1 = User()
        self.assertEqual(type(u1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        u1 = User()
        u2 = User()
        self.assertNotEqual(u1.id, u2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        u1 = User()
        u2 = User()
        for inst in [u1, u2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(u1.id, u2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        u1 = User()
        self.assertTrue(hasattr(u1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        u1 = User()
        self.assertIsInstance(u1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        u1 = User()
        self.assertTrue(hasattr(u1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        u1 = User()
        self.assertIsInstance(u1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        u1 = User()
        diff = u1.updated_at - u1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(User().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(User().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(User().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        u1 = User()
        u1.id = "123456"
        u1.created_at = u1.updated_at = dt
        u1_str = u1.__str__()
        self.assertIn("[User] (123456)", u1_str)
        self.assertIn("'id': '123456'", u1_str)
        self.assertIn("'created_at': " + dt_repr, u1_str)
        self.assertIn("'updated_at': " + dt_repr, u1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        u1 = User()
        string = "[{}] ({}) {}".format(
          "User", u1.id, str(u1.__dict__))
        self.assertEqual(str(u1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        u1 = User()
        string = "[User] ({}) {}".format(
          u1.id, u1.__dict__)
        self.assertEqual(string, str(u1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        u1 = User(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(u1.id, "345")
        self.assertEqual(u1.created_at, dt)
        self.assertEqual(u1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        u1 = User(None)
        self.assertNotIn(None, u1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(User(), storage.all().values())


class TestUser_save_method(unittest.TestCase):
    """
    Unittest for User save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        u1 = User()
        updated_at_1 = u1.updated_at
        u1.save()
        updated_at_2 = u1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        u1 = User()
        sleep(0.1)
        updated_at_1 = u1.updated_at
        u1.save()
        updated_at_2 = u1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        u1.save()
        self.assertLess(updated_at_2, u1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        u1 = User()
        with self.assertRaises(TypeError):
          u1.save(None)


class TestUser_to_dict_method(unittest.TestCase):
    """
    Unittests for User to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        u1 = User()
        dic = u1.to_dict()
        self.assertNotEqual(dic, u1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        u1 = User()
        dic = u1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        u1 = User()
        self.assertTrue(dict, type(u1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        u1 = User()
        self.assertIn("id", u1.to_dict())
        self.assertIn("created_at", u1.to_dict())
        self.assertIn("updated_at", u1.to_dict())
        self.assertIn("__class__", u1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        u1 = User()
        dt = datetime.today()
        u1.id = "123456"
        u1.created_at = u1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'User',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(u1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        u1 = User()
        with self.assertRaises(TypeError):
           u1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        u1 = User()
        u1.name = "Test"
        u1.age = 5
        dic = u1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
