#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is none or type(roman_string) != str:
        return 0
    val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numberss = [val[c] for c in roman_string] + [0]
    res  = 0

    for x in range(len(numbers) - 1):
        if numbers[x] >= numbers[x + 1]:
            res += numbers[x]
        else:
            res -= numbers[x]
            return (res)
