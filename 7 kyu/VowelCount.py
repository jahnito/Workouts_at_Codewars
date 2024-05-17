'''
https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python


Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for i in sentence:
        if i in vowels:
            count += 1
    return count


if __name__ == '__main__':
    print(get_count('651i5da1f5w1eferhdo1rh'))