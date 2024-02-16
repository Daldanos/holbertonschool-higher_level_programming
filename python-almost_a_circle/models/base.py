#!/usr/bin/python3
"""
Deffine Base Class
"""
import json


class Base:
    """Base Model

    Private Class Attributes:
        __nb_object : Number of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new base

        Args:
            id : Id of new base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
