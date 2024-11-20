#!/usr/bin/python3
"""Test suite for the User class"""
import unittest
from models.user import User
from models.base_model import BaseModel
import os


class TestUserClass(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def test_user_inheritance(self):
        """Test that User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes_exist(self):
        """Test that User has the required attributes"""
        self.assertTrue(hasattr(User, 'email'))
        self.assertTrue(hasattr(User, 'password'))
        self.assertTrue(hasattr(User, 'first_name'))
        self.assertTrue(hasattr(User, 'last_name'))

    def test_user_attributes_default_values(self):
        """Test default values of User attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attribute_assignment(self):
        """Test assigning values to User attributes"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_create_with_kwargs(self):
        """Test creating a User with keyword arguments"""
        user_data = {
            'email': 'test@example.com',
            'password': 'secret',
            'first_name': 'Jane',
            'last_name': 'Smith'
        }
        user = User(**user_data)

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.password, 'secret')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Smith')

    def test_user_to_dict(self):
        """Test the to_dict method of User"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        user_dict = user.to_dict()

        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_user_str_representation(self):
        """Test string representation of User"""
        user = User()
        user.email = "test@example.com"
        user.first_name = "John"

        str_rep = str(user)
        self.assertIn("[User]", str_rep)
        self.assertIn(user.id, str_rep)

    def test_multiple_user_instances(self):
        """Test creating multiple User instances"""
        user1 = User()
        user2 = User()

        self.assertNotEqual(user1.id, user2.id)
        self.assertNotEqual(user1.created_at, user2.created_at)

    def test_user_save_method(self):
        """Test the save method of User"""
        user = User()
        user.email = "test@example.com"
        
        # Store the initial updated_at
        initial_updated_at = user.updated_at
        
        # Call save method
        user.save()
        
        # Check that updated_at has changed
        self.assertNotEqual(initial_updated_at, user.updated_at)


if __name__ == '__main__':
    unittest.main()
