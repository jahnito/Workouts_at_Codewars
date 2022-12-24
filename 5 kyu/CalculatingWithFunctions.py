'''
https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

    There must be a function for each number from 0 ("zero") to 9 ("nine")
    There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
    Each calculation consist of exactly one operation and two numbers
    The most outer function represents the left operand, the most inner function represents the right operand
    Division should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))

'''

# Old solution
# def zero(f=False):
#     if f:
#         return f(0)
#     else:
#         return 0
# def one(f=False):
#     if f:
#         return f(1)
#     else:
#         return 1
# def two(f=False):
#     if f:
#         return f(2)
#     else:
#         return 2
# def three(f=False):
#     if f:
#         return f(3)
#     else:
#         return 3
# def four(f=False):
#     if f:
#         return f(4)
#     else:
#         return 4
# def five(f=False):
#     if f:
#         return f(5)
#     else:
#         return 5
# def six(f=False):
#     if f:
#         return f(6)
#     else:
#         return 6
# def seven(f=False):
#     if f:
#         return f(7)
#     else:
#         return 7
# def eight(f=False):
#     if f:
#         return f(8)
#     else:
#         return 8
# def nine(f=False):
#     if f:
#         return f(9)
#     else:
#         return 9

# def plus(n=0):
#     func = lambda x: x + n
#     return func
# def minus(n=0):
#     func = lambda x: x - n
#     return func
# def times(n=1):
#     func = lambda x: x * n
#     return func
# def divided_by(n=1):
#     func = lambda x: x // n
#     return func

def zero(action=None):
    if action:
        return action(0)
    else:
        return 0


def one(action=None):
    if action:
        return action(1)
    else:
        return 1


def two(action=None):
    if action:
        return action(2)
    else:
        return 2


def three(action=None):
    if action:
        return action(3)
    else:
        return 3


def four(action=None):
    if action:
        return action(4)
    else:
        return 4


def five(action=None):
    if action:
        return action(5)
    else:
        return 5


def six(action=None):
    if action:
        return action(6)
    else:
        return 6


def seven(action=None):
    if action:
        return action(7)
    else:
        return 7


def eight(action=None):
    if action:
        return action(8)
    else:
        return 8


def nine(action=None):
    if action:
        return action(9)
    else:
        return 9


def plus(a):
    return lambda x: x + a


def minus(a):
    return lambda x: x - a


def times(a):
    return lambda x: x * a


def divided_by(a):
    return lambda x: x // a


print(seven(times(five())))
