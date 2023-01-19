#!/usr/bin/python3
'''
https://www.codewars.com/kata/52bc74d4ac05d0945d00054e

Написать функцию first_non_repeating_letter на вход которой подайтся строка, и возврашает первый не повторяющийся символ нигде в строке.

Для примера, если получена строка 'stress', функция вернёт 't', поскольку буква t единожды встречается в строке, при этом первая такая в строке.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("") or None -- see sample tests.
'''

def first_non_repeating_letter(string: str):
    for i in string:
        if string.lower().count(i.lower()) == 1:
            return i
    return ''

if __name__ == '__main__':
    print(first_non_repeating_letter('stress'))
