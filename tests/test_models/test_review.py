#!/usr/bin/python3
"""The ``test_review`` module
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """The test suite for the Review class
    """
    def test_class_attribute_place_id(self):
        """The test case for the place_id attribute
        """
        review = Review()
        self.assertIsInstance(review.place_id, str)

    def test_class_attribute_user_id(self):
        """The test case for the user_id attribute
        """
        review = Review()
        self.assertIsInstance(review.user_id, str)

    def test_class_attribute_text(self):
        """The test case for the text attribute
        """
        review = Review()
        self.assertIsInstance(review.text, str)
