#!/usr/bin/python3
def print_reverse_alphabet():
    for ascii_code in range(ord('z'), ord('A') - 1, -1):
        print(chr(ascii_code), end='')
        if ascii_code != ord('A'):
            print(chr(ascii_code - (ord('a') - ord('A'))), end='')

print_reverse_alphabet()
