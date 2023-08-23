'''
Some Circles

https://www.codewars.com/kata/56143efa9d32b3aa65000016


Write a function that takes as its parameters one or more numbers which are the diameters of circles.

The function should return the total area of all the circles, rounded to the nearest integer in a string that says "We have this much circle: xyz".

You don't know how many circles you will be given, but you can assume it will be at least one.

So:

sum_circles(2) == "We have this much circle: 3"
sum_circles(2, 3, 4) == "We have this much circle: 23"

Translations and comments (and upvotes!) welcome!
Fundamentals Geometry Algebra
'''
import math

def sum_circles(*args):
    return f'We have this much circle: {round(sum(map(lambda x: math.pi * (x/2) ** 2, args)))}'
    

if __name__ == '__main__':
    print(sum_circles(2))
    print(sum_circles(2, 3, 4))
