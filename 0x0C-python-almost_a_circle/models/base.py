#!/usr/bin/python3
"""models file for base class"""

class base:
"""a representation of the base model"""

 __nb_objects = 0

def __init__(self, id=None):
        """Class constructor."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
