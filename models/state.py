#!/usr/bin/python3
"""The ``state`` module
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherit from the BaseModel

    Args:
        name(str): The name of the state
    """
    name = ""
