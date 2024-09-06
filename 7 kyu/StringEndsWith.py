'''
String ends with?

https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

Strings
Fundamentals
'''

def solution(text, ending):
    if isinstance(text, str) and isinstance(ending, str):
        wend = len(ending)
        if text[wend * -1:] == ending:
            return True
    return False


if __name__ == '__main__':
    fixed_tests_True = (
    ( "samurai", "ai"    ),
    ( "ninja",   "ja"    ),
    ( "sensei",  "i"     ),
    ( "abc",     "abc"   ),
    ( "abcabc",  "bc"    ),
    ( "fails",   "ails"  ),
)
    for i in fixed_tests_True:
        print(solution(i[0], i[1]))

    fixed_tests_False = (
    ( "sumo",    "omo"   ),
    ( "samurai", "ra"    ),
    ( "abc",     "abcd"  ),
    ( "ails",    "fails" ),
    ( "this",    "fails" ),
    ( "spam",    "eggs"  )
)
    
    for i in fixed_tests_False:
        print(solution(i[0], i[1]))
