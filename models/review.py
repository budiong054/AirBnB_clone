#!/usr/bin/python3
"""The ``review`` module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class inherit from ``BaseModel``

    Args:
        place_id(str): The place id
        user_id(str): The user id
        text(str): The review text
    """
    place_id = ""
    user_id = ""
    text = ""
