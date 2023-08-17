'''
https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python


You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

Examples:(Input --> Output)

121 --> 144
625 --> 676
114 --> -1 since 114 is not a perfect square

Algebra
Fundamentals
'''

# def find_next_square(sq):
#     num = sq ** 0.5

#     if int(num) < num:
#         result = -1
#     else:
#         result = int((num + 1) ** 2)
    
#     return result

def find_next_square(sq):
    num = sq ** 0.5
    if num.is_integer():
        result = int((num + 1) ** 2)
    else:
        result = -1
    return result


if __name__ == '__main__':
    print(find_next_square(196))