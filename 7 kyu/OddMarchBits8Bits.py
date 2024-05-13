'''
https://www.codewars.com/kata/58ee4db3e479611e6f000086

Odd bits are getting ready for Bits Battles.

Therefore the n bits march from right to left along an 8 bits path. Once the most-significant bit reaches the left their march is done. Each step will be saved as an array of 8 integers.

Return an array of all the steps.

1 <= n <= 8

NOTE: n != 0, because n represents the number of 1s.
Examples

This resembles a simple 8 LED chaser:

n = 3

00000111
00001110
00011100
00111000
01110000
11100000

n = 7

01111111
11111110
'''


def bit_march (n : int) -> list:
    nb = [0 for i in range(8 - n)] + [1 for i in range(n)]
    result = [nb]
    for i in range(8):
        if nb[0] == 0:
            nb = nb[1:] + [nb[0]]
            result.append(nb)
        else:
            break

    return result


if __name__ == "__main__":
    print(bit_march(3))