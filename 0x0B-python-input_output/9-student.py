#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the attributes of the Student inst
        """
        result_dict = {}

        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                result_dict[key] = value

        return result_dict
