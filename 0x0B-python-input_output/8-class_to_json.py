#!/usr/bin/python3
"""This module defines a Python class-to-JSON function"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        dict: A dictionary representing the object for JSON serialization.
    """
    result_dict = {}

    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result_dict[key] = value

    return result_dict
