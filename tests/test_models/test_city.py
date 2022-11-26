#!/usr/bin/python3
"""The ``test_city`` module
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """The test suite for the City class
    """
    def test_class_attribute_name(self):
        """Test case for the name attribute
        """
        my_city = City()
        self.assertIsInstance(my_city.name, str)

    def test_class_attribute_state_id(self):
        """The test case for the state_id attribute
        """
        my_city = City()
        self.assertIsInstance(my_city.state_id, str)
