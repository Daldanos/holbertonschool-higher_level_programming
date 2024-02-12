#!/usr/bin/python3
"""

Function to read a file and print it

"""


def read_file(filename=""):
    """Open a file and print it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
