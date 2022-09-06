#!/usr/bin/python3

from .rectangle import Rectangle
"""Class for square"""


class Square(Rectangle):
    """These class inherit from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """it instantiate the square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """It is called when print the class"""
        return ("[Square] ({}) {}/{} - {}".format(str(self.id),
        str(self.x), str(self.y), str(self.height)))

    @property
    def size(self):
        """It returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        """It set the size"""
        self.heihgt = value
        self.width = value

    def update(self, *args, **kwargs):
        """It update the values of the rectangle"""
        if len(args) > 0:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if len(args) > 1:
            self.width = args[1]
            self.height = args[1]
        elif 'size' in kwargs:
            self.width = kwargs['size']
            self.height = kwargs['size']
        if len(args) > 2:
            self.x = args[2]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if len(args) > 3:
            self.y = args[3]
        elif 'y' in kwargs:
            self.y = kwargs['y']

    def to_dictionary(self): 
        """It returns dictionary representation of a Square"""
        dicti = {"id": self.id, "x": self.x, "size": self.size, 
        "y": self.y}
        return dicti
