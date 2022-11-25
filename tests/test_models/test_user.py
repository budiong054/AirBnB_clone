#!/usr/bin/python3
"""The ``test_user`` module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """This class provide a test suite for the User class
    """
    def test_class_attribute_email(self):
        """This test case test the class attribute ``email`` for
            correct instance
        """
        user = User()
        self.assertIsInstance(user.email, str)

    def test_class_attribute_password(self):
        """This test case test the class attribute ``password``
            for correct instance
        """
        user = User()
        self.assertIsInstance(user.password, str)
    
    def test_class_attribute_first_name(self):
        """This test case test the class attribute ``first_name``
            for correct instance
        """
        user = User()
        self.assertIsInstance(user.first_name, str)
    
    def test_class_attribute_last_name(self):
        """This test case test the class attribute ``last_name``
            for correct instance
        """
        user = User()
        self.assertIsInstance(user.last_name, str)
