#!/usr/bin/python3
"""Module 100-my_int
Creates a class that inherits from int
"""


class MyInt(int):
    """
    MyInt is a subclass of int with inverted == and != operators.
    """

    def __eq__(self, other):
        """
        Invert the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the != operator.
        """
        return super().__eq__(other)
