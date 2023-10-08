'''


The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]

Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
Algorithms
Lists
Dynamic Programming
Fundamentals
Performance


'''


def max_sequence(arr):
    if all([i < 0 for i in arr]):
        return 0
    n = len(arr)
    x = 0
    for i in range(n):
        for j in range(n - 1,0,-1):
            print(j,end=' ')
        print()

            




# def max_sequence(arr):
#     if all([i < 0 for i in arr]):
#         return 0
#     else:
#         x = 0
#         n = len(arr)
#         for i in range(n):
#             for j in range(i,n):
#                 if x < sum(arr[i:j+1]):
#                 # print(arr[i:j+1])
#                     x = sum(arr[i:j+1])
#     return x




if __name__ == '__main__':
    # print(max_sequence([-1, -2, -100, - 50, -7]))
    print(max_sequence([-1, -2, -100, - 50, 12]))
    # print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
