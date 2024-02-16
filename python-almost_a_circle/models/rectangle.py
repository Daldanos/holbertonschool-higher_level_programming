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
