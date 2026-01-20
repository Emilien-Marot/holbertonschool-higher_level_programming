#!/usr/bin/python3
def roman_to_int(roman_string):
    dict_rom = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}

    if roman_string is None or not isinstance(roman_string, str):
        return 0
    i = False
    val = 0
    prev = None
    for letter in roman_string:
        if letter not in dict_rom.keys():
            return 0
        digit = dict_rom[letter]
        if prev is not None:
            if prev < digit:
                val -= prev
            else:
                val += prev
        prev = digit
    val += prev
    return val
