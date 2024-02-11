#!/usr/bin/python3
"""

Class Rectangle

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle definition"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return (((str(self.print_symbol) * self.__width + "\n") *
                self.__height).rstrip())

    def area(self):
        return (self.__width * self.__height)
