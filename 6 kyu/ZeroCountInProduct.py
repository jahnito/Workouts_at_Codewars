'''Zero count in product
https://www.codewars.com/kata/639dd2efd424cc0016e7a611/train/python

Description

You will need to write a function that takes sum as an argument, and returns a list. In this list there should be one or more nested lists; in each of them - three natural numbers ( including 0 ), so that the sum of this three numbers equals sum, and the product of this numbers is ending with us much zeroes as possible. You will need to find all solutions. The sum will be from 1 to 500, so you can use bruteforce. Feel free to create programm that can work not only for 3, but for any amount of numbers! Note that you will need to output only unique sets of numbers in ascending order.
Examples

zero_count(407) = [[32, 125, 250]] # 32, 125 and 250 is the only three numbers with sum of 407, that after multiplication have 6 zeroes. Other numbers have less
zero_count(199) = [[10, 64, 125], [24, 25, 150], [24, 50, 125], [24, 75, 100], [34, 40, 125]] # there is 5 possible solutions
zero_count(3) = [[0, 0, 3], [0, 1, 2]] # 2 solutions, each of them give 1 trailing zero
'''
import time

def zero_count(s):

    def count_zeros(n):
        if n == 0:
            return 1
        c = 0
        a = 0
        while a == 0:
            n //= 10
            c += 1
            a = n % 10
        return c

    result = []
    zeros = 0

    for a in range(0, s + 1):

        for b in range(0, s + 1):
            if a > b or sum([a, b]) > s:
                continue

            for c in range(0, s + 1):
                if b > c or a > c or sum([a, b, c]) != s:
                    continue
                else:
                    s_numbers = sum([a, b, c])

                    if s_numbers == s and str(a * b * c).endswith('0'):
                        if count_zeros(a * b * c) > zeros:
                            zeros = count_zeros(a * b * c)
                            result = []
                            result.append([a, b, c])
                        elif count_zeros(a * b * c) == zeros:
                            result.append([a, b, c])
    return result


if __name__ == '__main__':
    print(zero_count(499))
