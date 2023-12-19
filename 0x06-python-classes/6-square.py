class Square:
    """
    This class represents a square with private attributes

    Attributes:
    - __size (int): The size of the square.
    - __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class.

        Parameters:
        - size (int): The size of the square. Defaults to 0.
        - position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.__size = size
        self.__position = position
        self.__validate_size()
        self.__validate_position()

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Parameters:
        - value (int): The size to be set.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position attribute.

        Parameters:
        - value (tuple): The position to be set.

        Raises:
        - TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __validate_size(self):
        """
        Validates the size attribute.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def __validate_position(self):
        """
        Validates the position attribute.

        Raises:
        - TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(self.__position, tuple)
            or len(self.__position) != 2
            or not all(isinstance(i, int) for i in self.__position)
            or not all(i >= 0 for i in self.__position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square using the character '#'.

        If size is equal to 0, print an empty line.
        Position should be used by using space
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
