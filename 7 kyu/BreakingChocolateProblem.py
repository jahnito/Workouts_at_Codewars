'''
https://www.codewars.com/kata/534ea96ebb17181947000ada/train/python

Your task is to split the chocolate bar of given dimension n x m into small squares. Each square is of size 1x1 and unbreakable. Implement a function that will return minimum number of breaks needed.
For example if you are given a chocolate bar of size 2 x 1 you can split it to single squares in just one break, but for size 3 x 1 you must do two breaks.
If input data is invalid you should return 0 (as in no breaks are needed if we do not have any chocolate to split). Input will always be a non-negative integer.

Algorithms
'''

def break_chocolate(n, m):
    hi_zero = lambda x: x > 0
    if any([hi_zero(i) for i in (n, m)]):
        return (n - 1) + (m - 1) * n
    else:
        return 0


if __name__ == '__main__':
    print(break_chocolate(5, 5))
    print(break_chocolate(0, 0))
