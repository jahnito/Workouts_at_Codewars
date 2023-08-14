'''
https://www.codewars.com/kata/63d54b5d05992e0046752389/train/python

Description

You can paint an asperand by pixels in three steps:

    First you paint the inner square, with a side of k.
    Then you need to paint one pixel, that's laying diagonally relative to the inner square that you just painted ( the bottom-right corner of the inner square is touching the top-left corner of the pixel ). Let's call it the "bridge".
    Finally, you will need to paint the outer shape, connected diagonally to the "bridge" ( see the picture for more information ).

Here are some examples of this:
Your task is to find the number of pixels that need to be painted, for different k:

k = 1 => 11
k = 2 => 18
k = 3 => 26
k = 4 => 34

# Limitations are 1 ≤ k ≤ 1e9

'''

def count_pixels(k):
    if k > 2:
        r = k - 2
    else:
        r = 0
    square = k ** 2 - r ** 2
    walls = 4 * k + 6

    return square + walls


if __name__ == "__main__":
    print(count_pixels(4))
