#!/usr/bin/python3
"""

Class Rectangle

"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square definition from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
