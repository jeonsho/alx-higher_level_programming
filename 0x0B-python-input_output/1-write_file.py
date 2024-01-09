#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number

    Args:
        filename (str): The name of the file to write to.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.

    Note:
        - The function creates the file if it doesn't exist.
        - The function overwrites the content of the file if it already exists.
        - The file is assumed to be in UTF-8 encoding.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        nb_characters = file.write(text)
    return nb_characters
