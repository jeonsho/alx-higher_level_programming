#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                        'C': 100, 'D': 500, 'M': 1000}
    result = 0

    if not isinstance(roman_string, str) or len(roman_string) == 0:
        return 0

    for i in range(len(roman_string)):
        current_value = roman_dictionary[roman_string[i]]
        next_value = (
            roman_dictionary.get(roman_string[i + 1], 0)
            if i + 1 < len(roman_string) else 0
        )

        if current_value < next_value:
            result -= current_value
        else:
            result += current_value

    return result
