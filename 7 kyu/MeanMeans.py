'''
https://www.codewars.com/kata/57c6b44f58da9ea6c20003da/train/python

Take a list of n numbers a1, a2, a3, ..., aN to start with.

Arithmetic mean (or average) is the sum of these numbers divided by n.

Geometric mean (or average) is the product of these numbers taken to the nth root.
Example

List of numbers: 1, 3, 9, 27, 81

    n = 5
    Arithmetic mean = (1 + 3 + 9 + 27 + 81) / 5 = 121 / 5 = 24.2
    Geometric mean = (1 * 3 * 9 * 27 * 81) ^ (1/5) = 59049 ^ (1/5) = 9

Task

You will be given a list of numbers and their arithmetic mean. However, the list is missing one number. Using this information, you must figure out and return the geometric mean of the FULL LIST, including the number that's missing.
'''

def geo_mean(nums: list, arith_mean):

    def fact(nums):
        result = 1
        for i in nums:
            result *= i
        return result

    nums.append(arith_mean * (len(nums) + 1) - sum(nums))
    result = fact(nums) ** (1/len(nums))
    return result


if __name__ == '__main__':
    print(geo_mean([2], 10))