'''
https://www.codewars.com/kata/52223df9e8f98c7aa7000062

Description:

How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.

Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

Test examples:

"EBG13 rknzcyr." -->
"ROT13 example."

"This is my first ROT13 excercise!" -->
"Guvf vf zl svefg EBG13 rkprepvfr!"
'''


def rot13(message):
    result = ''
    for i in message:
        if (65 <= ord(i) <= 90) and ord(i) + 13 <= 90:
            result += chr(ord(i) + 13)
        elif (65 <= ord(i) <= 90) and ord(i) + 13 > 90:
            result += chr(ord(i) - 13)
        elif (97 <= ord(i) <= 122) and ord(i) + 13 <= 122:
            result += chr(ord(i) + 13)
        elif (97 <= ord(i) <= 122) and ord(i) + 13 > 122:
            result += chr(ord(i) - 13)
        else:
            result += i
    return result


if __name__ == '__main__':
    print(rot13(input()))
