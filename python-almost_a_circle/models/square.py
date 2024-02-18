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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """Update square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary of Rectangle"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }

