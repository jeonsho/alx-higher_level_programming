#!/usr/bin/python3
""" Create a rectangle class """


class Rectangle:
    """
    Class Rectangle that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
        value (int): The new width of the rectangle.
        Raises:
        TypeError: If the width is not an integer.
        ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
        value (int): The new height of the rectangle.
        Raises:
        TypeError: If the height is not an integer.
        ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
