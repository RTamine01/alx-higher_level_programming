#!/usr/bin/python3
"""models file for base class"""

class base:
"""a representation of the base of oop hierarchy"""

__nb_objects = 0
def __init__(self, id=None):
if id is not None:
self.id = id
else:
Base.__nb_objects += 1
self.id = Base.__nb_objects
