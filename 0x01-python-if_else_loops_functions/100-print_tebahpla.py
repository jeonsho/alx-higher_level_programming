#!/usr/bin/python3
def print_reverse_alphabet():
    for ascii_code in range(ord('z'), ord('A') - 1, -1):
        letter = chr(ascii_code)
        if 'a' <= letter <= 'z':
            print("{}".format(letter), end='')
        else:
            print("{}".format(letter.lower()), end='')

print_reverse_alphabet()

