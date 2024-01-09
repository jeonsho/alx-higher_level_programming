#!/usr/bin/python3
"""This module defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """
    Return the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON string to be converted to a Python object.

    Returns:
        object: The Python data structure represented by the input JSON string.
    """
    return json.loads(my_str)
