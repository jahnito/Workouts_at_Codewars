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
import math

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
    # s / y == s - x
    # 9 / 3 == 9 - 6 => 3 + 6 == 3 * 3
    B = 0
    while True:
        a = B * y
        b = B + x
        if math.floor(a) == b and x < 0:
            return B + x
        if math.ceil(a) == b and x > 0:
            return B + x

        B += 1


if __name__ == '__main__':
    print(age(6, 3))
    print(age(-15, 0.25))