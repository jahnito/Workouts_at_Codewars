'''
https://www.codewars.com/kata/517abf86da9663f1d2000003

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
'''

def to_camel_case(text: str):
    for i in '-_':
        text = text.replace(i, ' ')
    return ''.join([w if i == 0  else w.capitalize() for i, w in enumerate(text.split())])


if __name__ == '__main__':
    print(to_camel_case('the-stealth-warrior'))
    print(to_camel_case('The_Stealth_Warrior'))
