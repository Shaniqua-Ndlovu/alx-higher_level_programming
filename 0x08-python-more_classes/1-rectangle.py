#!/usr/bin/python3
""" Using Python3 """


class Rectangle:
    """Rectangle Class"""
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        "Retrieves the width of the rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        "Sets the width of the rectangle"
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        "Retrieve the height of the rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        "Set the height of the rectangle"
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
<<<<<<< HEAD
            raise ValueError("height must be >= 0")
=======
            raise ValueError('height must be >= 0')
>>>>>>> 3b56b9db7e386e2c68408208f0269ef751508139
        self.__height = value
