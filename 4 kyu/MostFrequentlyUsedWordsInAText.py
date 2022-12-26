'''
https://www.codewars.com/kata/51e056fe544cf36c410000fb

Write a function that, given a string of text (possibly with punctuation and
line-breaks), returns an array of the top-3 most occurring words, in descending
order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more
    apostrophes (') in ASCII. Apostrophes can appear at the start, middle or
    end of a word ('abc, abc', 'abc', ab'c are all valid) Any other characters
    (e.g. #, \, / , . ...) are not part of a word and should be treated as
    whitespace. Matches should be case-insensitive, and the words in the
    result should be lowercased. Ties may be broken arbitrarily.     If a
    text contains fewer than three unique words, then either the top-2 or
    top-1 words should be returned, or an empty array if a text contains no
    words.

Examples:

top_3_words("In a village of La Mancha, the name of which I have no desire
to call to mind, there lived not long since one of those gentlemen that
keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound
for coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]

Bonus points (not really, but just for fun):

    Avoid creating an array whose memory footprint is roughly as big as the
    input text. Avoid sorting the entire array of unique words.
'''


def top_3_words(text: str):
    result = {}
    # We form a list of all ascii character indices other than letters and an apostrophe
    whitespaces = [i for i in range(33,39)] + [i for i in range(40,65)] + [i for i in range(91,97)] + [i for i in range(123,127)]
    # Replace with spaces
    for lt in whitespaces:
        text = text.replace(chr(lt), ' ')
    for i in [i.lower() for i in text.split()]:
        if not result.get(i):
            result[i] = 1
        else:
            result[i] = result.get(i) + 1
    data = [i[0] for i in sorted(result.items(), key=lambda x: x[1], reverse=True)[0:3] if i[0] and set(i[0]) != {"'"}]
    return data


test_text1 = '''
            In a village of La Mancha, the name of which I have no desire to call to
            mind, there lived not long since one of those gentlemen that keep a lance
            in the lance-rack, an old buckler, a lean hack, and a greyhound for
            coursing. An olla of rather more beef than mutton, a salad on most
            nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
            on Sundays, made away with three-quarters of his income.
            '''


test_text2 = """ test#''''''te''h'j'''"""


print(top_3_words(test_text2))
