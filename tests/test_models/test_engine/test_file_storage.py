#!/usr/bin/python3
"""Defines unittest for model/engine/file_storage.py.
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFilesStorage_instantiation(unittest.TestCase):
    """Unittest for testing the instantiation of the FileStorage class."""
    
    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_file_path(self):
        self.assertIsInstance(FileStorage._FileStorage__file_path, str,
                              "File path must be a string")
        self.assertTrue(FileStorage._FileStorage__file_path.endswith('.json'),
                        "File path must end with a json")


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up test environment before each test method"""
        # Clear the storage before each test
        FileStorage._FileStorage__objects = {}
        # Ensure we're using a test file
        FileStorage._FileStorage__file_path = "test_file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test method"""
        # Remove the test file if it exists
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        # Reset the storage
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test the all() method"""
        # Initially, objects should be empty
        self.assertEqual(self.storage.all(), {})

        # Create a test object and add it
        test_obj = BaseModel()
        self.storage.new(test_obj)

        # Check if the object is in the storage
        stored_objects = self.storage.all()
        self.assertIn(f"BaseModel.{test_obj.id}", stored_objects)
        self.assertEqual(stored_objects[f"BaseModel.{test_obj.id}"], test_obj)

    def test_new_method(self):
        """Test the new() method"""
        # Create a test object
        test_obj = BaseModel()
        self.storage.new(test_obj)

        # Check if the object was added with the correct key
        expected_key = f"BaseModel.{test_obj.id}"
        self.assertIn(expected_key, self.storage.all())
        self.assertEqual(self.storage.all()[expected_key], test_obj)

    def test_save_method(self):
        """Test the save() method"""
        # Create a test object
        test_obj = BaseModel()
        self.storage.new(test_obj)
        
        # Save the object
        self.storage.save()

        # Check if the file was created
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        # Check the contents of the file
        with open(FileStorage._FileStorage__file_path, 'r') as f:
            saved_data = json.load(f)

        # Verify the saved data
        expected_key = f"BaseModel.{test_obj.id}"
        self.assertIn(expected_key, saved_data)
        self.assertEqual(saved_data[expected_key], test_obj.to_dict())

    def test_reload_method(self):
        """Test the reload() method"""
        # Create and save an object
        original_obj = BaseModel()
        original_key = f"BaseModel.{original_obj.id}"
        self.storage.new(original_obj)
        self.storage.save()

        # Clear the current storage
        FileStorage._FileStorage__objects = {}

        # Reload the storage
        self.storage.reload()

        # Check if the object was reloaded
        reloaded_objects = self.storage.all()
        self.assertIn(original_key, reloaded_objects)
        
        # Check that the reloaded object is an instance of BaseModel
        reloaded_obj = reloaded_objects[original_key]
        self.assertIsInstance(reloaded_obj, BaseModel)
        
        # Verify the attributes match the original object
        self.assertEqual(reloaded_obj.id, original_obj.id)

    def test_reload_nonexistent_file(self):
        """Test reload() when file doesn't exist"""
        # Remove the file if it exists
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

        # Attempt to reload
        # This should not raise an exception
        try:
            self.storage.reload()
        except Exception as e:
            self.fail(f"reload() raised {type(e).__name__} unexpectedly!")

    def test_multiple_objects(self):
        """Test storing multiple objects"""
        # Create multiple objects
        obj1 = BaseModel()
        obj2 = BaseModel()
        
        # Add objects to storage
        self.storage.new(obj1)
        self.storage.new(obj2)
        
        # Save and reload
        self.storage.save()
        
        # Clear current storage
        FileStorage._FileStorage__objects = {}
        
        # Reload
        self.storage.reload()
        
        # Check both objects are reloaded
        reloaded_objects = self.storage.all()
        self.assertEqual(len(reloaded_objects), 2)
        self.assertIn(f"BaseModel.{obj1.id}", reloaded_objects)
        self.assertIn(f"BaseModel.{obj2.id}", reloaded_objects)

if __name__ == '__main__':
    unittest.main()
