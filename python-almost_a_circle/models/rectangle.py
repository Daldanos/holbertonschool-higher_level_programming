#!/usr/bin/python3
"""Define a Rectangle Class."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new Rectangle.

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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the retangle"""
        return (self.width * self.height)

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.y, self.width, self.height))

    def display(self):
        """Prints rectangle with "#" Character"""
        for i in range(self.height):
            print("#" * self.width, end="")
            print()
