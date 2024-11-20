#!/usr/bin/python3
""" Contains city definition class """
from models.base_model import BaseModel


class City(BaseModel):
    """Defines city, inherits from BaseModel"""
    state_id = ""
    name = ""
