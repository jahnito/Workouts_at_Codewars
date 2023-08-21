'''
https://www.codewars.com/kata/53222010db0eea35ad000001/train/python


Task

Your challenge is to write a function named getSlope/get_slope/GetSlope that calculates the slope of the line through two points.
Input

Each point that the function takes in is an array 2 elements long. The first number is the x coordinate and the second number is the y coordinate. If the line through the two points is vertical or if the same point is given twice, the function should return null/None.


https://infofaq.ru/ugol-naklona-pryamoj.html
'''


def get_slope(p1, p2):
    x1, x2, y1, y2 = p1[0], p2[0], p1[1], p2[1]
    if x1 == x2 and y1 == y2 or x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)


if __name__ == '__main__':
    print(get_slope([11,1],[1,11]))
    print(get_slope([1,1],[2,2]))
    print(get_slope([124,16],[45,28]))