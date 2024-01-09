#!/usr/bin/python3
"""This module defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize into JSON.
        filename (str): The name of the file where the JSON will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
