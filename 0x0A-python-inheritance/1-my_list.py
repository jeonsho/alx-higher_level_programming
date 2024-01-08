#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """
    A custom class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
