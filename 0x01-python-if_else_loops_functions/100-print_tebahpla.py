#!/usr/bin/python3
def print_reverse_alphabet():
    for ascii_code in range(ord('z'), ord('A') - 1, -1):
        letter = chr(ascii_code)
        if 'a' <= letter <= 'z':
            print("{}".format(
                letter.upper() if (ascii_code - ord('A')) % 2 == 0 else letter
            ), end='')

print_reverse_alphabet()
