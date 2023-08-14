'''
https://www.codewars.com/kata/558445a88826e1376b000011

Description:

Julie is x years older than her brother, and she is also y times as old as him.

Given x and y calculate Julie's age using the function age(x, y).

For example:

age(6, 3) #returns 9

Note also that x can be negative, and y can be a decimal.

age(-15, 0.25) #returns 5

That is, Julie is 15 years younger and 0.25 times the age of her brother.

Do not concern yourself with the imperfections inherent in dividing by floating point numbers, as your answer will be rounded. Also, for the sake of simplicity, Julie is never the same age as her brother.
'''
from time import time

# def age(x, y):
#     s = 0
#     c = 0
#     while True:
#         c += 1
#         s += 1
#         if (s + x) / y == s:
#             print(c)
#             return s * y

def age(x, y):
    brother_age = x
    if x > 0:
        inc = x
    else:
        inc = -x
        x = -x
    fl = True

    while True:
        if (round(brother_age, 0) + x) / y == round(brother_age, 0):
            return round(brother_age, 0) + x
        elif (brother_age + x) / y > brother_age and fl:
            inc = (-inc / 2)
            fl = False
        elif (brother_age + x) / y < brother_age and not fl:
            inc = (-inc / 2)
            fl = True

        brother_age += inc


if __name__ == '__main__':
    start = time()
    print(age(6, 3))
    end = time()
    print(end)