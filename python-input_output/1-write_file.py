#!/usr/bin/python3
"""

Class Rectangle

"""


def write_file(filename="", text=""):
    """write to a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
