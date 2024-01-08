#!/usr/bin/python3
"""Module 10-square
Creates a square class
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

    def area(self):
        """
        Return the area of the Square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return the string representation of the Square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
