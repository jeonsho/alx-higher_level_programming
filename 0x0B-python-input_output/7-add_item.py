#!/usr/bin/python3
"""
This is a python script that adds all arguments to a Python list.
The list is then saved to a file named 'add_item.json'.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except FileNotFoundError:
        arg_list = []

    arg_list.extend(sys.argv[1:])
    save_to_json_file(arg_list, filename)
