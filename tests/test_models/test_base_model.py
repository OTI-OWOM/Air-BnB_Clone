import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    
    def test_instance_attributes(self):
        """Test the attributes of BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertTrue(uuid.UUID(model.id))  # Checks if id is a valid UUID
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method."""
        model = BaseModel()
        expected = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), expected)

    def test_save_method(self):
        """Test the save method updates updated_at."""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns correct dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model.id)
        self.assertEqual(model_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
