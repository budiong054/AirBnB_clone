#!/usr/bin/python3
"""The ``amenity`` module
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherit from the BaseModel
    
    Args:
        name(str): The name of the amenity
    """
    name = ""
