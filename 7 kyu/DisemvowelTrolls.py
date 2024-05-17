'''
https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

Disemvowel Trolls

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
'''

def disemvowel(string_):
    vowels = 'euioaEUIOA'
    result = []
    for i in string_:
        if i not in vowels:
            result.append(i)
    return ''.join(result)


if __name__ == '__main__':
    print(disemvowel('This website is for losers LOL!'))