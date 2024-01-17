'''
https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3


Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''

def abbrev_name(name: str):
    return '{0}.{1}'.format(*[i[0].upper() for i in name.split()])


if __name__ == '__main__':
    print(abbrev_name('Test test'))