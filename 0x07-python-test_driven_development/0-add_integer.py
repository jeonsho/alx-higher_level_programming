#!/usr/bin/python3
"""A function that adds two integers."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Prototype: def add_integer(a, b=98):
    Returns an integer: the addition of a and b
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
