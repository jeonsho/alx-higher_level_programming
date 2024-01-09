#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
