'''
https://www.codewars.com/kata/545cedaa9943f7fe7b000048

A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(s: str) -> bool:
    for i in range(97,123):
        if chr(i) not in s.lower():
            return False
    return True


print(is_pangram('abc'))
print(is_pangram('The quick brown fox jumps over the lazy dog'))
