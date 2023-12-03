#!/usr/bin/python3
def no_c(my_string):
    rel_str = ''.join(char for char in my_string if char.lower() not in {'c'})

    return rel_str
