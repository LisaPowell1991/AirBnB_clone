#!/usr/bin/python3
"""
The Unittest for Review
"""
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.review import Review


class TestReview_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of Review class
    """
    def test_instantiation(self):
        """
        Test instantiation of Review class
        """
        r1 = Review()
        self.assertIsInstance(r1, Review)
        self.assertEqual(str(
          type(r1)), "<class 'models.review.Review'>")
        self.assertTrue(issubclass(type(r1), Review))

    def test_instantiation_with_id(self):
        """
        Test instantiation of Review class with id
        """
        r1 = Review()
        self.assertTrue(hasattr(r1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        r1 = Review()
        self.assertEqual(type(r1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        r1 = Review()
        r2 = Review()
        for inst in [r1, r2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(r1.id, r2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        r1 = Review()
        self.assertTrue(hasattr(r1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        r1 = Review()
        self.assertIsInstance(r1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        r1 = Review()
        self.assertTrue(hasattr(r1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        r1 = Review()
        self.assertIsInstance(r1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        r1 = Review()
        diff = r1.updated_at - r1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(Review().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(Review().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(Review().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        r1 = Review()
        r1.id = "123456"
        r1.created_at = r1.updated_at = dt
        r1_str = r1.__str__()
        self.assertIn("[Review] (123456)", r1_str)
        self.assertIn("'id': '123456'", r1_str)
        self.assertIn("'created_at': " + dt_repr, r1_str)
        self.assertIn("'updated_at': " + dt_repr, r1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        r1 = Review()
        string = "[{}] ({}) {}".format(
          "Review", r1.id, str(r1.__dict__))
        self.assertEqual(str(r1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        r1 = Review()
        string = "[Review] ({}) {}".format(
          r1.id, r1.__dict__)
        self.assertEqual(string, str(r1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        r1 = Review(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(r1.id, "345")
        self.assertEqual(r1.created_at, dt)
        self.assertEqual(r1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        r1 = Review(None)
        self.assertNotIn(None, r1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(Review(), storage.all().values())


class TestReview_save_method(unittest.TestCase):
    """
    Unittest for Review save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        r1 = Review()
        updated_at_1 = r1.updated_at
        r1.save()
        updated_at_2 = r1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        r1 = Review()
        sleep(0.1)
        updated_at_1 = r1.updated_at
        r1.save()
        updated_at_2 = r1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        r1.save()
        self.assertLess(updated_at_2, r1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        r1 = Review()
        with self.assertRaises(TypeError):
            r1.save(None)


class TestReview_to_dict_method(unittest.TestCase):
    """
    Unittests for Review to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        r1 = Review()
        dic = r1.to_dict()
        self.assertNotEqual(dic, r1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        r1 = Review()
        dic = r1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        r1 = Review()
        self.assertTrue(dict, type(r1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        r1 = Review()
        self.assertIn("id", r1.to_dict())
        self.assertIn("created_at", r1.to_dict())
        self.assertIn("updated_at", r1.to_dict())
        self.assertIn("__class__", r1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        r1 = Review()
        dt = datetime.today()
        r1.id = "123456"
        r1.created_at = r1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'Review',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(r1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        r1 = Review()
        with self.assertRaises(TypeError):
            r1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        r1 = Review()
        r1.name = "Test"
        r1.age = 5
        dic = r1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
