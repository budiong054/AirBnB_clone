#!/usr/bin/python3
"""The ``test_file_storage`` module

This contains a test class for the file_storage module
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """This class provide a test suite for the FileStorage class
    """
    def test_raises_error_for_private_attribute(self):
        """Check if it raises error when trying to access the
            private attribute ``file path`` and ``objects``
        """
        fs = FileStorage()
        with self.assertRaises(AttributeError):
            fs.__file_path
        with self.assertRaises(AttributeError):
            fs.__object

    def test_all_method(self):
        """This test the all method for right return type
        """
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_new_method(self):
        """This test the `new` method for right behaviour
        """
        b = BaseModel()
        fs = FileStorage()
        fs.new(b)
        fs_keys = fs.all().keys()
        self.assertIn(f'{b.__class__.__name__}.{b.id}', fs_keys)

    def test_save_method(self):
        """This test the save method
        """
        fs = FileStorage()
        fs.save()

    def test_reload_method(self):
        """This test the reload method
        """
        fs = FileStorage()
        #print(fs.all())
        fs.reload()
