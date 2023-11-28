#!/usr/bin/python3
def uppercase(s):
    for char in s:
        uppercase_char = (
            chr(ord(char) - (ord('a') - ord('A')))
            if 'a' <= char <= 'z'
            else char
        )
        print("{:s}".format(uppercase_char), end="")
    print("")
