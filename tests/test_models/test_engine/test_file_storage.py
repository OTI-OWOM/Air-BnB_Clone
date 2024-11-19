import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

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

    def test_file_storage_private_attributes(self):
        """
        Test FileStorage private attributes specific to the given implementation
        """
        # Test __file_path
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'), 
                        "__file_path should be a class attribute")
    
        # Verify __file_path is a string
        file_path = FileStorage._FileStorage__file_path
        self.assertIsInstance(file_path, str, 
                        "__file_path must be a string")
    
        # Verify __file_path is not empty
        self.assertTrue(file_path, 
                        "__file_path cannot be an empty string")
    
        # Check file path characteristics
        self.assertTrue(file_path.endswith('.json'), 
                        "__file_path should end with .json")

        # Test __objects
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'), 
                        "__objects should be a class attribute")
    
        # Verify __objects is a dictionary
        objects = FileStorage._FileStorage__objects
        self.assertIsInstance(objects, dict, 
                        "__objects must be a dictionary")
    
        # Specific to your implementation
        # Since the class is explicitly setting __objects to an empty dict
        self.assertEqual(len(objects), 0, 
                        "__objects should be empty")

if __name__ == '__main__':
    unittest.main()
