'''
https://www.codewars.com/kata/5583d268479559400d000064/train/python

Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.
'''

def binary_to_string(binary):
    words = ''
    while binary:
        words += chr(int(binary[0:8], 2))
        binary = binary[8:]
    return words


if __name__ == '__main__':
    print(binary_to_string('0100100001100101011011000110110001101111'))