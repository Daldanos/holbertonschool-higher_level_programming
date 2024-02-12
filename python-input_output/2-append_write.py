#!/usr/bin/python3
"""

Class Rectangle

"""


def append_write(filename="", text=""):
    """Append text to a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
