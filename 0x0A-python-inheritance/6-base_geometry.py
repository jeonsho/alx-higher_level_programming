#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area() method.
    """

    def area(self):
        """
        Public instance method that raises an Exception with the message
        'area() is not implemented.'
        """
        raise Exception("area() is not implemented")
