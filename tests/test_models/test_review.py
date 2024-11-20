#!/usr/bin/python3
"""Test suite for the Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReviewClass(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def test_review_inheritance(self):
        """Test that Review inherits from BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes_exist(self):
        """Test that Review has all the required attributes"""
        attributes = ['place_id', 'user_id', 'text']
        for attr in attributes:
            self.assertTrue(hasattr(Review, attr), f"Missing attribute: {attr}")

    def test_review_attributes_default_values(self):
        """Test default values of Review attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_attribute_assignment(self):
        """Test assigning values to Review attributes"""
        review = Review()
        review.place_id = "place123"
        review.user_id = "user456"
        review.text = "Great place! Highly recommended."

        self.assertEqual(review.place_id, "place123")
        self.assertEqual(review.user_id, "user456")
        self.assertEqual(review.text, "Great place! Highly recommended.")

    def test_review_create_with_kwargs(self):
        """Test creating a Review with keyword arguments"""
        review_data = {
            'place_id': 'place789',
            'user_id': 'user101',
            'text': 'Amazing experience, would stay again!'
        }
        review = Review(**review_data)

        self.assertEqual(review.place_id, 'place789')
        self.assertEqual(review.user_id, 'user101')
        self.assertEqual(review.text, 'Amazing experience, would stay again!')

    def test_review_to_dict(self):
        """Test the to_dict method of Review"""
        review = Review()
        review.place_id = "place456"
        review.user_id = "user789"
        review.text = "Wonderful stay"

        review_dict = review.to_dict()

        self.assertIn('place_id', review_dict)
        self.assertIn('user_id', review_dict)
        self.assertIn('text', review_dict)
        self.assertEqual(review_dict['place_id'], "place456")
        self.assertEqual(review_dict['user_id'], "user789")
        self.assertEqual(review_dict['text'], "Wonderful stay")

    def test_review_str_representation(self):
        """Test string representation of Review"""
        review = Review()
        review.text = "Fantastic accommodation"

        str_rep = str(review)
        self.assertIn("[Review]", str_rep)
        self.assertIn(review.id, str_rep)

    def test_multiple_review_instances(self):
        """Test creating multiple Review instances"""
        review1 = Review()
        review2 = Review()

        self.assertNotEqual(review1.id, review2.id)
        self.assertNotEqual(review1.created_at, review2.created_at)

    def test_review_attribute_types(self):
        """Test the types of the Review attributes"""
        review = Review()
        
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

    def test_review_empty_attributes(self):
        """Test creating a Review with empty attributes"""
        review = Review()
        review.place_id = ""
        review.user_id = ""
        review.text = ""

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_long_text(self):
        """Test assigning a long text to the review"""
        review = Review()
        long_text = "A very long review that describes the experience in great detail. " * 10
        review.text = long_text

        self.assertEqual(review.text, long_text)

    def test_review_special_characters(self):
        """Test assigning text with special characters"""
        review = Review()
        review.text = "Great place! 5/5 stars. Highly recommended. 😊"

        self.assertEqual(review.text, "Great place! 5/5 stars. Highly recommended. 😊")


if __name__ == '__main__':
    unittest.main()
