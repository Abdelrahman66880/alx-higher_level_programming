#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting the correct value of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of the rectangle"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setting the value of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
  
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if (self.__height) == 0 or (self.__width) == 0:
            return (0)
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print a repersintation of the rectangle using #"""
        if (self.height) == 0 or (self.width) == 0:
            return (0)
        
        rect = []
        for i in range(self.__height):
            rect.append("#" * self.__width)
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
    
    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
