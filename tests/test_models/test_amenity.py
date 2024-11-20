#!/usr/bin/python3
"""Test suite for the Amenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os


class TestAmenityClass(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity()

    def test_amenity_inheritance(self):
        """Test that Amenity inherits from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attribute_exists(self):
        """Test that Amenity has the required attribute"""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_amenity_attribute_default_value(self):
        """Test default value of Amenity attribute"""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_attribute_assignment(self):
        """Test assigning value to Amenity attribute"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_create_with_kwargs(self):
        """Test creating an Amenity with keyword arguments"""
        amenity_data = {
            'name': 'Gym'
        }
        amenity = Amenity(**amenity_data)
        self.assertEqual(amenity.name, 'Gym')

    def test_amenity_to_dict(self):
        """Test the to_dict method of Amenity"""
        amenity = Amenity()
        amenity.name = "Spa"

        amenity_dict = amenity.to_dict()

        self.assertIn('name', amenity_dict)
        self.assertEqual(amenity_dict['name'], "Spa")

    def test_amenity_str_representation(self):
        """Test string representation of Amenity"""
        amenity = Amenity()
        amenity.name = "Sauna"

        str_rep = str(amenity)
        self.assertIn("[Amenity]", str_rep)
        self.assertIn(amenity.id, str_rep)

    def test_multiple_amenity_instances(self):
        """Test creating multiple Amenity instances"""
        amenity1 = Amenity()
        amenity2 = Amenity()

        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertNotEqual(amenity1.created_at, amenity2.created_at)

    def test_amenity_save_method(self):
        """Test the save method of Amenity"""
        amenity = Amenity()
        amenity.name = "Fitness Center"
        
        # Store the initial updated_at
        initial_updated_at = amenity.updated_at
        
        # Call save method
        amenity.save()
        
        # Check that updated_at has changed
        self.assertNotEqual(initial_updated_at, amenity.updated_at)

    def test_amenity_empty_name(self):
        """Test creating an Amenity with an empty name"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_name_reassignment(self):
        """Test multiple name reassignments"""
        amenity = Amenity()
        amenity.name = "Initial Amenity"
        self.assertEqual(amenity.name, "Initial Amenity")

        amenity.name = "Updated Amenity"
        self.assertEqual(amenity.name, "Updated Amenity")

    def test_amenity_attribute_type(self):
        """Test the type of the name attribute"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_name_with_special_characters(self):
        """Test assigning a name with special characters"""
        amenity = Amenity()
        amenity.name = "24/7 Concierge Service"
        self.assertEqual(amenity.name, "24/7 Concierge Service")

    def test_amenity_long_name(self):
        """Test assigning a long name"""
        amenity = Amenity()
        long_name = "A very long amenity name that describes a complex service offering"
        amenity.name = long_name
        self.assertEqual(amenity.name, long_name)

    def test_amenity_unicode_name(self):
        """Test assigning a name with unicode characters"""
        amenity = Amenity()
        amenity.name = "Café & Lounge"
        self.assertEqual(amenity.name, "Café & Lounge")


if __name__ == '__main__':
    unittest.main()
