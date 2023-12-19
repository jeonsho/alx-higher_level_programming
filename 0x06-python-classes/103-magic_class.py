#!/usr/bin/python3
"""Magic class from a given ByteCode."""


import math


class MagicClass:
    """
    This class represents a magical circle.

    It allows calculating the area and circumference of the circle
    based on the provided radius.

    Attributes:
    - radius (float): The radius of the magical circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a new instance of MagicClass with a specified radius.

        Parameters:
        - radius (float): The radius of the magical circle. Defaults to 0.
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the magical circle.

        Returns:
        - float: The area of the magical circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the magical circle.

        Returns:
        - float: The circumference of the magical circle.
        """
        return 2 * math.pi * self.__radius


def perform_special_magic():
    """
    Performs a special magic operation.

    Returns:
    - str: A magical result from the special operation.
    """
    return "Abracadabra! You've witnessed the magic."
