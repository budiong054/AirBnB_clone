#!/usr/bin/python3
"""This defines the Airbnb console using cmd serving as frontend (for interaction)."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User



