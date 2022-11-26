#!/usr/bin/python3
"""The ``test_amenity`` module
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """The test suite for the Amenity class
    """
    def test_class_attribute_name(self):
        """Test case for the name attribute
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
