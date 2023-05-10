'''
Complete the solution so that the function will break up camel casing, using a space between words.
Example

"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""



'''
def solution(s):
    return ''.join(i if i.islower() else ' ' + i for i in s)


if __name__ == "__main__":
    print(solution('helloWorld'))