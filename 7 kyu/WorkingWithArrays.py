'''
Working with arrays

https://www.codewars.com/kata/5a4ff3c5fd56cbaf9800003e

In this kata the function returns an array/list of numbers without its last element. The function is already written for you and the basic tests pass, but random tests fail. Your task is to figure out why and fix it.

Good luck!

Hint: watch out for side effects.

def without_last(lst):
    # Fix it
    lst.pop() # removes the last element
    return lst
'''

def without_last(lst):
    return lst[:-1]