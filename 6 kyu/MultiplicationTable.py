'''Description:

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]

https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08
'''

def multiplication_table(n):
    return [[j * i for j in range(1, n + 1)] for i in range(1, n + 1) ]

# def multiplication_table(n):
#     result = []
#     for i in range(1, n + 1):
#         result.append([j * i for j in range(1, n + 1)])
#     return result

if __name__ == "__main__":
    print(multiplication_table(3))