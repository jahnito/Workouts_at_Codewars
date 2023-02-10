'''
https://www.codewars.com/kata/58dced7b702b805b200000be/train/python

This series of katas will introduce you to basics of doing geometry with computers.

Point objects have attributes x and y.

Write a function calculating distance between Point a and Point b.

Tests compare expected result and actual answer with tolerance of 1e-6.
'''
from preloaded import Point


def distance_between_points(a, b):
    cat1 = abs(a.x - b.x)
    cat2 = abs(a.y - b.y)
    return (cat1 ** 2 + cat2 ** 2) ** 0.5


if __name__ == '__main__':
    a = [int(input()) for i in range(2)]
    b = [int(input()) for i in range(2)]
    print(distance_between_points(a, b))
