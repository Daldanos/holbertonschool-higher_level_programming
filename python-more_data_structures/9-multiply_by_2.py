#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied = a_dictionary.copy()
    multiplied.update(
            (key, value * 2) for key, value in multiplied.items()
            )
    return multiplied
