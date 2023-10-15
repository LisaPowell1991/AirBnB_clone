#!/usr/bin/python3
"""
The Unittest for BaseModel
"""
import unittest
from datetime import datetime
from time import sleep

from models import storage
from models.base_model import BaseModel


class TestBaseModel_Instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of BaseModel class
    """
    def test_instantiation(self):
        """
        Test instantiation of BaseModel class
        """
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(str(
          type(b1)), "<class 'models.base_model.BaseModel'>")
        self.assertTrue(issubclass(type(b1), BaseModel))

    def test_instantiation_with_id(self):
        """
        Test instantiation of BaseModel class with id
        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "id"))

    def test_instantiation_id_type(self):
        """
        Test instantiation of id type
        """
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    def test_distinct_ids(self):
        """
        Test distinct ids of two instances
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_instantiation_uuid(self):
        """
        Test that id is a uuid
        """
        b1 = BaseModel()
        b2 = BaseModel()
        for inst in [b1, b2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(b1.id, b2.id)

    def test_instantiation_created_at(self):
        """
        Test that created_at exists in instantiation
        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "created_at"))

    def test_instantiation_created_at_type(self):
        """
        Test that created_at is a datetime
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    def test_instantiation_updated_at(self):
        """
        Test that updated_at exists in instantiation
        """
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, "updated_at"))

    def test_instantiation_updated_at_type(self):
        """
        Test that updated_at is a datetime
        """
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)

    def test_instantiation_datetime(self):
        """
        Tests that created_at and updated_at are same at creation
        """
        datetime.now()
        b1 = BaseModel()
        diff = b1.updated_at - b1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 1)

    def test_instantiation_id_public(self):
        """
        Test that id is public
        """
        self.assertEqual(str, type(BaseModel().id))

    def test_instantiation_created_at_public(self):
        """
        Test that created_at is public
        """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_instantiation_updated_at_public(self):
        """
        Test that updated_at is public
        """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_instantiation_str_method(self):
        """
        Test that str method is string representation
        """
        dt = datetime.today()
        dt_repr = repr(dt)
        b1 = BaseModel()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        b1_str = b1.__str__()
        self.assertIn("[BaseModel] (123456)", b1_str)
        self.assertIn("'id': '123456'", b1_str)
        self.assertIn("'created_at': " + dt_repr, b1_str)
        self.assertIn("'updated_at': " + dt_repr, b1_str)

    def test_instantiation_str_return(self):
        """
        Test that str returns the correct output type
        """
        b1 = BaseModel()
        string = "[{}] ({}) {}".format(
          "BaseModel", b1.id, str(b1.__dict__))
        self.assertEqual(str(b1), string)

    def test_instantiation_str_return_2(self):
        """
        Test that str returns the correct output type 2
        """
        b1 = BaseModel()
        string = "[BaseModel] ({}) {}".format(b1.id, b1.__dict__)
        self.assertEqual(string, str(b1))

    def test_instantantiation_with_args_kwargs(self):
        """
        Test instantiation with used args and kwargs
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b1 = BaseModel(
          "12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b1.id, "345")
        self.assertEqual(b1.created_at, dt)
        self.assertEqual(b1.updated_at, dt)

    def test_instantiation_without_kwargs(self):
        """
        Test instantiation with unused kwargs
        """
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_without_args(self):
        """
        Test instantiation with unused args
        """
        b1 = BaseModel(None)
        self.assertNotIn(None, b1.__dict__.values())

    def test_instantiation_storage(self):
        """
        Test if new instance is stored in storage
        """
        self.assertIn(BaseModel(), storage.all().values())


class TestBaseModel_save_method(unittest.TestCase):
    """
    Unittest for BaseModel save method
    """
    def test_instantiation_save(self):
        """
        Test if save method saves instance to storage
        """
        b1 = BaseModel()
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertNotEqual(updated_at_1, updated_at_2)

    def test_instantiation_save_2(self):
        """
        Test if save method saves instance to storage multiple times
        """
        b1 = BaseModel()
        sleep(0.1)
        updated_at_1 = b1.updated_at
        b1.save()
        updated_at_2 = b1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.1)
        b1.save()
        self.assertLess(updated_at_2, b1.updated_at)

    def test_instantiation_save_with_arg(self):
        """
        Test if save method takes argument
        """
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.save(None)


class TestBaseModel_to_dict_method(unittest.TestCase):
    """
    Unittests for BaseModel to_dict method
    """
    def test_instantiation_to_dict(self):
        """
        Test if to_dict method returns a dictionary
        """
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertNotEqual(dic, b1.__dict__)

    def test_instantiation_to_dict_datetime(self):
        """
        Test if to_dict method returns created_at
        and updated_at as strings
        """
        b1 = BaseModel()
        dic = b1.to_dict()
        self.assertEqual(type(dic['created_at']), str)
        self.assertEqual(type(dic['updated_at']), str)

    def test_instantiation_to_dict_type(self):
        """
        Test to_dict output type
        """
        b1 = BaseModel()
        self.assertTrue(dict, type(b1.to_dict()))

    def test_instantiation_to_dict_keys(self):
        """
        Test to_dict keys
        """
        b1 = BaseModel()
        self.assertIn("id", b1.to_dict())
        self.assertIn("created_at", b1.to_dict())
        self.assertIn("updated_at", b1.to_dict())
        self.assertIn("__class__", b1.to_dict())

    def test_instantiation_to_dict_output(self):
        """
        Test to_dict output
        """
        b1 = BaseModel()
        dt = datetime.today()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        dic = {
          'id': '123456',
          '__class__': 'BaseModel',
          'created_at': dt.isoformat(),
          'updated_at': dt.isoformat()
        }
        self.assertDictEqual(b1.to_dict(), dic)

    def test_instantiation_to_dict_with_arg(self):
        """
        Test to_dict with arguments
        """
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b1.to_dict(None)

    def test_instantiation_to_dict_with_attributes(self):
        """
        Test to_dict with extra attributes
        """
        b1 = BaseModel()
        b1.name = "Test"
        b1.age = 5
        dic = b1.to_dict()
        attrb = [
          "id", "created_at", "updated_at", "name", "age", "__class__"]
        self.assertCountEqual(attrb, dic.keys())
        self.assertEqual(dic["name"], "Test")
        self.assertEqual(dic["age"], 5)


if __name__ == "__main__":
    unittest.main()
