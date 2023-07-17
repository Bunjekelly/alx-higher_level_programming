#!/usr/bin/python3

"""a rectangle class that inherits from base"""

import sys
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the class"""

        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrives x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle with #"""
        rectangle = ""
        for i in range(self.y):
            rectangle += "\n"
        for k in range(self.__height):
            rectangle += ' ' * self.x + "#" * self.__width
            if k != self.__height - 1:
                rectangle += "\n"
        print(rectangle, file=sys.stdout)
        return rectangle

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        v = f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
        return v

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        attribute = ['id', 'width', 'height', 'x', 'y']
        if args:
            index = 0
            for arg in args:
                setattr(self, attribute[index], arg)
                index += 1
        else:
            for key, value in kwargs.items():
                return (key, value)

    def to_dictionary(self):
        """"returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height":  self.height, "x": self.x, "y": self.y}
