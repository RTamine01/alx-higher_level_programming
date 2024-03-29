#!/usr/bin/python3
"""task: inherits_from"""


def inherits_from(obj, a_class):
    """function that returns Truesi the object is an instance of a class
     that inherited (directly or indirectly) from the specified class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
