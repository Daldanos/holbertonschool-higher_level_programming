#!/usr/bin/python3
"""
Define a Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nj_objects

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
