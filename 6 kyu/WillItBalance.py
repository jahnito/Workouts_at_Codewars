'''
https://www.codewars.com/kata/5a8328fefd57777fa3000072/train/python

A stick is balanced horizontally on a support. Will it topple over or stay balanced? (This is a physics problem: imagine a real wooden stick balanced horizontally on someone's finger or on a narrow table, for example).
The stick is represented as a list, where each entry shows the mass in that part of the stick.
The stick is balanced on a support. The "terrain" is represented by a list of 1s and 0s, where the 1s represent the support and the 0s represent empty space. Each index is a coordinate on the x-axis, so e.g. the physical interpretations of some terrains are as follows:

The stick will only balance if its centre of mass is directly above some part of its support. Return True if the stick will balance and False if it will topple.

Both lists will be of equal length (that is, the stick and the terrain have equal width so that each index of the stick is directly above the corresponding index of the terrain). Every terrain will contain one, and only one, support.
Examples:
[2,3,2]
[0,1,0] ---> Perfectly balanced, return True

[5,1,1]
[0,1,0] ---> will topple to the left, return False

[3,3,4]
[0,1,0] ---> will topple to the right (but only just)

[7,1,1,1,1,1,1,1]
[0,1,1,0,0,0,0,0] ---> will balance, perfectly, without a doubt

[5, 3, 2, 8, 6]
[0, 0, 0, 1, 1] ---> will topple to the left
'''

def will_it_balance(stick: list, terrain: list):
    if terrain.count(1) == 1:
        s = f = terrain.index(1)
    else:
        s = terrain.index(1)
        f = s + terrain.count(1) - 1
    if len(stick[0:s]) and len(stick[f+1:]):
        return sum(stick[0:s+1]) == sum(stick[f:])
    elif len(stick[0:s]) == 0:
        return sum(stick[0:s+1]) < sum(stick[f:])
    else:
        return sum(stick[0:s+1]) > sum(stick[f:])



if __name__ == "__main__":
    tests = (([2,3,2],[0,1,0]), 
             ([5,1,1],[0,1,0]), 
             ([3,3,4],[0,1,0]), 
             ([9,7,1,1],[1,1,0,0]), 
             ([9,1,1,7],[1,1,0,0]),
             )

    for i,j in tests:
        print(will_it_balance(i,j))