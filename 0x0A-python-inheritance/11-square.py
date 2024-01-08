#!/usr/bin/python3
"""Module 11-square
Creates a Square Class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with private size,
        validated by integer_validator.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return the string representation of the Square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
