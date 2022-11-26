#!/usr/bin/python3
"""The ``test_state`` module
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """The test suite for the State class
    """
    def test_class_attribute_name(self):
        """Test case for the name attribute
        """
        my_state = State()
        self.assertIsInstance(my_state.name, str)
