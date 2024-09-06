'''
https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
'''

def count(s: str):
    res = {}
    if s:
        for i in s:
            if i not in res:
                res[i] = s.count(i)
    return res


if __name__ == '__main__':
    print(count('aba'))
    print(count(''))
    print(count('aa'))
    print(count('aabb'))
