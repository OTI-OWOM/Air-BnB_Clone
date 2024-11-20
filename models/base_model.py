#!/usr/bin/python3
"""This module contains the base Model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines a simple base class that other model can inherit from"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            # If created from a dictionary (e.g., from JSON)
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        # Converts string time stamp to datetime
                        setattr(self, key,
                                datetime.strptime(value, time_format))
                    else:
                        setattr(self, key, value)
        else:
            # New Instance creation
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
