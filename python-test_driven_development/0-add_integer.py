#!/usr/bin/python3

"""
Module to define an add integer.

"""


def add_integer(a, b=98):
    """define function"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float):
            a = int(a)
        if isinstance(b, float):
            b = int(b)
        c = a + b
    return c
