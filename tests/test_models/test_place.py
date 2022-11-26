#!/usr/bin/python3
"""The ``test_place`` module
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """The test suite for the Place class
    """
    def test_class_attribute_city_id(self):
        """The test case for the city_id attribute
        """
        place = Place()
        self.assertIsInstance(place.city_id, str)

    def test_class_attribute_user_id(self):
        """The test case for the user_id attribute
        """
        place = Place()
        self.assertIsInstance(place.user_id, str)

    def test_class_attribute_name(self):
        """The test case for the name attribute
        """
        place = Place()
        self.assertIsInstance(place.name, str)

    def test_class_attribute_description(self):
        """The test case for the description attribute
        """
        place = Place()
        self.assertIsInstance(place.description, str)

    def test_class_attribute_number_rooms(self):
        """The test case for the number_rooms attribute
        """
        place = Place()
        self.assertIsInstance(place.number_rooms, int)

    def test_class_attribute_number_bathrooms(self):
        """The test case for the number_bathrooms attribute
        """
        place = Place()
        self.assertIsInstance(place.number_bathrooms, int)

    def test_class_attribute_max_guest(self):
        """The test case for the max_guest attribute
        """
        place = Place()
        self.assertIsInstance(place.max_guest, int)

    def test_class_attribute_price_by_night(self):
        """The test case for the price_by_night attribute
        """
        place = Place()
        self.assertIsInstance(place.price_by_night, int)

    def test_class_attribute_latitude(self):
        """The test case for the latitude attribute
        """
        place = Place()
        self.assertIsInstance(place.latitude, float)

    def test_class_attribute_longitude(self):
        """The test case for the longitude attribute
        """
        place = Place()
        self.assertIsInstance(place.longitude, float)

    def test_class_attribute_amenity_ids(self):
        """The test case for the amenity_ids attribute
        """
        place = Place()
        self.assertIsInstance(place.amenity_ids, list)
