#!/usr/bin/python3

""" class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """defining a square class that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the class"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return [Square] (<id>) <x>/<y> - <size>"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """retrieves the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value <= 0:
            raise ValueError("value must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """sets arguments"""
        if args:
            vars = ["id", "size", "x", "y"]
            for index, value in enumerate(args):
                if index == 1:
                    setattr(self, "height", value)
                    setattr(self, "width", value)
                else:
                    setattr(self, vars[index], value)
        else:
            for key, value in kwargs.items():
                if key == "size":
                    setattr(self, "height", value)
                    setattr(self, "width", value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
