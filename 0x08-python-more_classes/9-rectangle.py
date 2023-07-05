#!/usr/bin/python3

"""a class Rectangle that defines a rectangle
by width and height and public instance
method area and perimeter"""


class Rectangle:
    """defining the class"""
    number_of_instances = 0
    print_symbol = '#'

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance
        with width == height == size"""
        return Rectangle(size, size)

    def __init__(self, width=0, height=0):
        """initializing the class"""

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def area(self):
        """defining the rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """defining the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """defining the width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """defining the height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.width
            if i < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """eturn a string representation of the rectangle to be
        able to recreate a new instance by using eval"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting an instance"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
