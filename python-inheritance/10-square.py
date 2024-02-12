#!/usr/bin/python3
"""

Class Rectangle

"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
