#!/usr/bin/python3
"""
Define a Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle

        Args:
            width (int): Width
            height (int): Height
            x (int): Coordinate x
            y (int): Coordinate y
            id (int): Identity of Rectangle

        Raises:
            TypeError: If not INT
            ValueError: If less than 0
            TypeError: If not INT
            VaLueError: If less than 0
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
        """Get width"""
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
        """Get Height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """Get X coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Get y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
