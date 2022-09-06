#!/usr/bin/python3

from .base import Base
"""Class Rectangle that inheri from Base Class"""



class Rectangle(Base):
    """Definition of Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the size of a width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the size of a width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get the size of the Height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Set the size of the Height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 1:
            raise TypeError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Set x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Set y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Get the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """It print the rectangle"""
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print('{}{}'.format(' ' * self.__x, '#' * self.__width))

    def __str__(self):
        """Overriding the __str__ method"""
        id = str(self.id)
        return ("[Rectangle] ({:s}) {:s}/{:s} - {:s}/{:s}".format(str(
            self.id), str(self.__x), str(self.__y), str(self.__width),
            str(self.__height)))

    def update(self, *args, **kwargs):
        """It update the values of the rectangle"""
        if len(args) > 0:
            self.id = args[0]
        elif 'id' in kwargs:
            self.id = kwargs['id']
        if len(args) > 1:
            self.width = args[1]
        elif 'width' in kwargs:
            self.width = kwargs['width']
        if len(args) > 2:
            self.height = args[2]
        elif 'height' in kwargs:
            self.height = kwargs['height']
        if len(args) > 3:
            self.x = args[3]
        elif 'x' in kwargs:
            self.x = kwargs['x']
        if len(args) > 4:
            self.y = args[4]
        elif 'y' in kwargs:
            self.y = kwargs['y']
    def to_dictionary(self): 
        """It returns dictionary representation of a Rectangle"""
        dicti = {"x": self.x, "y": self.y, "id": self.id,
        "height": self.height, "width": self.width}
        return dicti
