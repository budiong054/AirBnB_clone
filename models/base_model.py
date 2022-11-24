#!/usr/bin/python3
"""The ``base_model`` modules contains the ``BaseModel class
"""
#from models import storage
import models
from datetime import datetime
import uuid


class BaseModel():
    """The BaseModel is a parent class that takes care of initialization,
        serialization and deserialization
    """
    def __init__(self, *args, **kwargs):
        """Initializes the instance attribute
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return the str representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute `updated_at` with the
            current datetime
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of `__dict__`
            of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = new_dict['created_at'].isoformat()
        new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
