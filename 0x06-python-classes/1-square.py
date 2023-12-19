#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """
    The Square class represents a square with a private attribute `__size`.

    Attributes:
    - __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square.
        """

        self.__size = size
