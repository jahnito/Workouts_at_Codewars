'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''


# def move_zeros(lst):
#     res = [i for i in lst if i != 0]
#     zeros = [i for i in lst if i == 0]
#     res.extend(zeros)
#     return res


def move_zeros(lst: list) -> list:
    new_lst = [i for i in lst if i != 0] + [i for i in lst if i == 0]
    return new_lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
