'''
https://www.codewars.com/kata/5656b6906de340bd1b0000ac


Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
'''

def longest(a1, a2):
    '''
    Через множество избавляемся от дублирующихся букв, сортируем, объеденяем в строку
    '''
    return ''.join(sorted(set(a1+a2)))

a, b = input(), input()

print(longest(a, b))
