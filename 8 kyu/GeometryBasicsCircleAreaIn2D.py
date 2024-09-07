'''
https://www.codewars.com/kata/58e3f824a33b52c1dc0001c0/train/python

This series of katas will introduce you to basics of doing geometry with computers.

Write the function circleArea/CircleArea which takes in a Circle object and calculates the area of that circle.
The Circle class can be seen below:

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

And the Point class can be seen below:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
'''
from math import pi


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


def circle_area(circle: Circle):
    return pi * circle.radius ** 2


circles = [Circle((10, 10), 30), Circle((-15, 5),  12.5)]

if __name__ == '__main__':
    for i in circles:
        print(circle_area(i))
