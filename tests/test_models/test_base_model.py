#!/usr/bin/python3
"""This a test modules for the BaseModel class
"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """This class provide a test suite for the BaseModel class
    """
    def test_instance_attribute_id(self):
        """This test case test the instance attribute `id` for correct
            instance
        """
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_instance_attribute_created_at(self):
        """This test case test the instance attribute `create_at`
        """
        b_1 = BaseModel()
        self.assertIsInstance(b_1.created_at, datetime)

    def test_instance_attribute_updated_at(self):
        """This test case test the instance attribute `updates_at`
        """
        b_2 = BaseModel()
        self.assertIsInstance(b_2.updated_at, datetime)

    def test_basemodel_save_method(self):
        """This test the `save` method
        """
        b = BaseModel()
        b.save()
        self.assertIsInstance(b.updated_at, datetime)

    def test_basemodel_to_dict_method(self):
        """This test case test the to_dict method
        """
        b = BaseModel()
        b.to_dict()
        self.assertIsInstance(b.to_dict(), dict)

    def test_basemodel_to_dict_method_correct_type(self):
        """This test the ``to_dict`` method elements type
        """
        b = BaseModel()
        my_json = b.to_dict()
        self.assertEqual(type(my_json['created_at']), str)
        self.assertEqual(type(my_json['updated_at']), str)
        self.assertEqual(type(my_json['id']), str)
        self.assertEqual(type(my_json['__class__']), str)

    def test_create_BaseModel_from_dictionary(self):
        """This test case test the create BaseModel from dictionary
            model
        """
        b = BaseModel()
        my_b_json = b.to_dict()
        new_b = BaseModel(**my_b_json)
        self.assertEqual(new_b.id, b.id)
        self.assertEqual(type(new_b.created_at), datetime)
        self.assertEqual(type(new_b.updated_at), datetime)
        self.assertEqual(new_b.created_at, b.created_at)
        self.assertEqual(new_b.updated_at, b.updated_at)

    def test_two_object_if_there_are_same(self):
        """Test if the recreated object is the same as the original/first
            object
        """
        b = BaseModel()
        my_b_json = b.to_dict()
        new_b = BaseModel(**my_b_json)
        self.assertIsNot(b, new_b)
