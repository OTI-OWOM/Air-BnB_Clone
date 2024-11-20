#!/usr/bin/python3
"""Test suite for the Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up test environment"""
        self.place = Place()

    def test_place_inheritance(self):
        """Test that Place inherits from BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes_exist(self):
        """Test that Place has all the required attributes"""
        attributes = [
            'city_id', 'user_id', 'name', 'description', 
            'number_rooms', 'number_bathrooms', 'max_guest', 
            'price_by_night', 'latitude', 'longitude', 'amenity_ids'
        ]
        for attr in attributes:
            self.assertTrue(hasattr(Place, attr), f"Missing attribute: {attr}")

    def test_place_attributes_default_values(self):
        """Test default values of Place attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_attribute_assignment(self):
        """Test assigning values to Place attributes"""
        place = Place()
        place.city_id = "SF123"
        place.user_id = "user456"
        place.name = "Cozy Apartment"
        place.description = "Beautiful downtown apartment"
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "SF123")
        self.assertEqual(place.user_id, "user456")
        self.assertEqual(place.name, "Cozy Apartment")
        self.assertEqual(place.description, "Beautiful downtown apartment")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_place_create_with_kwargs(self):
        """Test creating a Place with keyword arguments"""
        place_data = {
            'city_id': 'NY123',
            'user_id': 'user789',
            'name': 'Luxury Loft',
            'description': 'Spacious loft in Manhattan',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 250,
            'latitude': 40.7128,
            'longitude': -74.0060,
            'amenity_ids': ['amenity3', 'amenity4']
        }
        place = Place(**place_data)

        self.assertEqual(place.city_id, 'NY123')
        self.assertEqual(place.user_id, 'user789')
        self.assertEqual(place.name, 'Luxury Loft')
        self.assertEqual(place.description, 'Spacious loft in Manhattan')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 250)
        self.assertEqual(place.latitude, 40.7128)
        self.assertEqual(place.longitude, -74.0060)
        self.assertEqual(place.amenity_ids, ['amenity3', 'amenity4'])

    def test_place_attribute_types(self):
        """Test the types of the Place attributes"""
        place = Place()
        
        self.assertIsInstance(place.city_id, str)
        self.assertIsInstance(place.user_id, str)
        self.assertIsInstance(place.name, str)
        self.assertIsInstance(place.description, str)
        
        self.assertIsInstance(place.number_rooms, int)
        self.assertIsInstance(place.number_bathrooms, int)
        self.assertIsInstance(place.max_guest, int)
        self.assertIsInstance(place.price_by_night, int)
        
        self.assertIsInstance(place.latitude, float)
        self.assertIsInstance(place.longitude, float)
        
        self.assertIsInstance(place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
