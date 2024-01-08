#!/usr/bin/python3
"""Module is_same_class
Finds if an object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class.
    """
    return type(obj) == a_class
