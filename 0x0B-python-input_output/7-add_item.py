#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""


import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

argv = sys.argv

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []

for i in range(1, len(argv)):
    content.append(argv[i])

save_to_json_file(content, filename)
