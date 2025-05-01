'''


Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
Regular Expressions
Strings


https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python
'''

def increment_string(strng: str) -> str:
    def nums(s: str) -> str:
        for i, c in enumerate(s):
            if c.isdigit() and s[i:].isdigit():
                return s[i:]

    def retnum(numline):
        full_len = len(numline)
        num = str(int(numline) + 1)
        zeros = full_len - len(num)
        if zeros > 0:
            return full_len, numline[:zeros] + num
        else:
            return full_len, num

    if strng == "" or strng[-1].isalpha():
        return strng + '1'
    elif strng:
        lc, num = retnum(nums(strng))
        return strng[:-lc] + num




if __name__ == '__main__':
    print(increment_string("631243220=4ce74536786053%E'D#39220SV;=E8074480000009"))
    print(increment_string('foobar23'))
    print(increment_string('foo0042'))
    print(increment_string('foo9'))
    print(increment_string('foo099'))
    print(increment_string('foo00'))
