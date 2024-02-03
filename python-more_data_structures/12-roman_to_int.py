#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    romandict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    k = 0
    result = 0

    for j in roman_string[::-1]:
        i = romandict[j]
        if i >= k:
            result += i
        else:
            result -= i
        k = i

    return result
