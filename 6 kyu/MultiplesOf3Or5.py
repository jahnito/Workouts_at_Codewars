'''
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once.

Courtesy of projecteuler.net (Problem 1)
'''

def solution(number):
    return  sum(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, (i for i in range(number)))))


if __name__ == '__main__':
    for i in [4,6,16,3,5,15,0,-1,10,20,200, -3]:
        print(solution(i))