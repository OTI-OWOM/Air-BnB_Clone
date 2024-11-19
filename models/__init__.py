#!/usr/bin/python3
""" Module contains instantiation of the FileStorage class"""
from models.engine.file_storage import FileStorage


# Create a unique storage instance for the entire application
storage = FileStorage()

# Reload existing data if any
storage.reload()
