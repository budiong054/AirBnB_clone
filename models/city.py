#!/usr/bin/python3
"""The ``city`` module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherit from the BaseModel

    Args:
        state_id(str): The state id
        name(str): The name of the city
    """
    state_id = ""
    name = ""
