'''
https://www.codewars.com/kata/557d9e4d155e2dbf050000aa/solutions/python

What is the answer to life the universe and everything

Create a function that will make anything true

    anything({}) != [],          'True'
    anything('Hello') < 'World', 'True'
    anything(80) > 81,           'True'
    anything(re) >= re,          'True'
    anything(re) <= math,        'True'
    anything(5) == ord,          'True'

Source: CheckIO
'''
import re
import math


class Any:
    def __init__(self, value):
        self.value = value

    def __lt__(self, any):
        return True
    
    def __gt__(self, any):
        return True

    def __eq__(self, any):
        return True
    
    def __ne__(self, any):
        return True

    def __le__(self, any):
        return True

    def __ge__(self, any):
        return True


def anything(thing):
    return Any(thing)

if __name__ == '__main__':
    print(anything({}) != [])
    print(anything('Hello') < 'World')
    print(anything(80) > 81)
    print(anything(re) >= re)