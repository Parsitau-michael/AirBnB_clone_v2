#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at'] and isinstance(value,
                                                                      str):
                    value = datetime.fromisoformat(value)

                setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
