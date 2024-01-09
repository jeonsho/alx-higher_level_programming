#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8) and return the number

    Args:
        filename (str): The name of the file to be appended to.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    Notes:
        - If the file doesn’t exist, it will be created.
        - The file is handled in append mode, so existing content is preserved.
        - The file is assumed to be in UTF-8 encoding.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
