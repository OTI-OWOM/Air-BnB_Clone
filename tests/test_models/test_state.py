#!/usr/bin/python3
"""Test suite for the State class"""
import unittest
from models.state import State
from models.base_model import BaseModel
import os


class TestStateClass(unittest.TestCase):
    """Test cases for the State class"""

    def setUp(self):
        """Set up test environment"""
        self.state = State()

    def test_state_inheritance(self):
        """Test that State inherits from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attribute_exists(self):
        """Test that State has the required attribute"""
        self.assertTrue(hasattr(State, 'name'))

    def test_state_attribute_default_value(self):
        """Test default value of State attribute"""
        self.assertEqual(self.state.name, "")

    def test_state_attribute_assignment(self):
        """Test assigning value to State attribute"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_state_create_with_kwargs(self):
        """Test creating a State with keyword arguments"""
        state_data = {
            'name': 'New York'
        }
        state = State(**state_data)
        self.assertEqual(state.name, 'New York')

    def test_state_to_dict(self):
        """Test the to_dict method of State"""
        state = State()
        state.name = "Texas"

        state_dict = state.to_dict()

        self.assertIn('name', state_dict)
        self.assertEqual(state_dict['name'], "Texas")

    def test_state_str_representation(self):
        """Test string representation of State"""
        state = State()
        state.name = "Florida"

        str_rep = str(state)
        self.assertIn("[State]", str_rep)
        self.assertIn(state.id, str_rep)

    def test_multiple_state_instances(self):
        """Test creating multiple State instances"""
        state1 = State()
        state2 = State()

        self.assertNotEqual(state1.id, state2.id)
        self.assertNotEqual(state1.created_at, state2.created_at)

    def test_state_save_method(self):
        """Test the save method of State"""
        state = State()
        state.name = "Washington"
        
        # Store the initial updated_at
        initial_updated_at = state.updated_at
        
        # Call save method
        state.save()
        
        # Check that updated_at has changed
        self.assertNotEqual(initial_updated_at, state.updated_at)

    def test_state_empty_name(self):
        """Test creating a State with an empty name"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_name_reassignment(self):
        """Test multiple name reassignments"""
        state = State()
        state.name = "Initial State"
        self.assertEqual(state.name, "Initial State")

        state.name = "Updated State"
        self.assertEqual(state.name, "Updated State")

    def test_state_attribute_type(self):
        """Test the type of the name attribute"""
        state = State()
        self.assertIsInstance(state.name, str)


if __name__ == '__main__':
    unittest.main()
