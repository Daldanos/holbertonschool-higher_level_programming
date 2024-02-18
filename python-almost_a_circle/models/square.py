#!/usr/bin/python3
"""Define a Square Class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): Size
            x (int): x coordinate
            y (int): y coordinate
            id (int): Id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square size."""
        return self.__width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))
