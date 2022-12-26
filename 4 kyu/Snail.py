'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

Description:
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
'''

'''
Solve

Step 1
                        Flipping the array to move values to index zero (1, 2, 3)
   +---+---+---+    +---+---+---+
0  | 1 | 2 | 3 |  0 | 8 | 9 | 4 |              +---+---+---+
   +---+---+---+    +---+---+---+     RESULT = | 1 | 2 | 3 |
1  | 8 | 9 | 4 |  1 | 7 | 6 | 5 |              +---+---+---+
   +---+---+---+    +---+---+---+
2  | 7 | 6 | 5 |
   +---+---+---+

Step 2
                        Flipping the array to move values to index zero (4, 5)
   +---+---+         +---+---+
0  | 4 | 5 |       0 | 9 | 6 |              +---+---+---+     +---+---+
   +---+---+         +---+---+     RESULT = | 1 | 2 | 3 |  +  | 4 | 5 |
1  | 9 | 6 |       1 | 8 | 7 |              +---+---+---+     +---+---+
   +---+---+         +---+---+
2  | 8 | 7 |
   +---+---+

Step any
...
'''


def snail(snail_map: list) -> list:
    result = snail_map[0]
    del snail_map[0]
    while snail_map:
        snail_map = [i[::-1] for i in snail_map]
        snail_map = [[snail_map[j][i] for j in range(len(snail_map))] for i in range(len(snail_map[0]))]
        result.extend(snail_map[0])
        del snail_map[0]
    return result


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]


print(snail(array))

# my old solution
# def snail(snail_map):
#     n = len(snail_map)
#     res_map = []
#     x, y, mx, my = 0, 0, 1, 0
#     if len(snail_map) == 1 and not snail_map[0]:
#         return res_map
#     for _ in range(n**2):
#         res_map.append(snail_map[y][x])
#         snail_map[y][x] = None
#         if x + mx == n:
#             mx, my = my, mx
#         elif y + my == n:
#             mx, my = -1, 0
#         elif x + mx < 0:
#             mx, my = my, mx
#         elif not snail_map[y + my][x + mx] and my == -1:
#             mx, my = 1, 0
#         elif not snail_map[y + my][x + mx] and mx == 1:
#             mx, my = my, mx
#         elif not snail_map[y + my][x + mx] and my == 1:
#             mx, my = -1, 0
#         elif not snail_map[y + my][x + mx] and mx == -1:
#             mx, my = my, mx

#         x, y = x + mx, y + my

#     return res_map
