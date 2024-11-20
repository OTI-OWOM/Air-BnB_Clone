#!/usr/bin/python3
"""Test suite for the City class"""
import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCityClass(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def test_city_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes_exist(self):
        """Test that City has the required attributes"""
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))

    def test_city_attributes_default_values(self):
        """Test default values of City attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_attribute_assignment(self):
        """Test assigning values to City attributes"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_create_with_kwargs(self):
        """Test creating a City with keyword arguments"""
        city_data = {
            'state_id': 'NY',
            'name': 'New York City'
        }
        city = City(**city_data)

        self.assertEqual(city.state_id, 'NY')
        self.assertEqual(city.name, 'New York City')

    def test_city_to_dict(self):
        """Test the to_dict method of City"""
        city = City()
        city.state_id = "TX"
        city.name = "Houston"

        city_dict = city.to_dict()

        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)
        self.assertEqual(city_dict['state_id'], "TX")
        self.assertEqual(city_dict['name'], "Houston")

    def test_city_str_representation(self):
        """Test string representation of City"""
        city = City()
        city.name = "Chicago"

        str_rep = str(city)
        self.assertIn("[City]", str_rep)
        self.assertIn(city.id, str_rep)

    def test_multiple_city_instances(self):
        """Test creating multiple City instances"""
        city1 = City()
        city2 = City()

        self.assertNotEqual(city1.id, city2.id)
        self.assertNotEqual(city1.created_at, city2.created_at)

    def test_city_save_method(self):
        """Test the save method of City"""
        city = City()
        city.state_id = "WA"
        city.name = "Seattle"
        
        # Store the initial updated_at
        initial_updated_at = city.updated_at
        
        # Call save method
        city.save()
        
        # Check that updated_at has changed
        self.assertNotEqual(initial_updated_at, city.updated_at)

    def test_city_empty_attributes(self):
        """Test creating a City with empty attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_attribute_reassignment(self):
        """Test multiple attribute reassignments"""
        city = City()
        city.state_id = "CA"
        city.name = "Los Angeles"
        
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "Los Angeles")

        city.state_id = "NY"
        city.name = "Buffalo"
        
        self.assertEqual(city.state_id, "NY")
        self.assertEqual(city.name, "Buffalo")

    def test_city_attribute_types(self):
        """Test the types of the attributes"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_with_partial_kwargs(self):
        """Test creating a City with partial keyword arguments"""
        city = City(state_id="CA")
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "")

        city = City(name="San Diego")
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "San Diego")


if __name__ == '__main__':
    unittest.main()
