'''
https://www.codewars.com/kata/58e0f0bf92d04ccf0a000010

Count all the sheep on farm in the heights of New Zealand



Every Friday and Saturday night, farmer counts amount of sheep returned back to his farm (sheep returned on Friday stay and don't leave for a weekend).

Sheep return in groups each of the days -> you will be given two arrays with these numbers (one for Friday and one for Saturday night). Entries are always positive ints, higher than zero.

Farmer knows the total amount of sheep, this is a third parameter. You need to return the amount of sheep lost (not returned to the farm) after final sheep counting on Saturday.

Example 1: Input: {1, 2}, {3, 4}, 15 --> Output: 5

Example 2: Input: {3, 1, 2}, {4, 5}, 21 --> Output: 6

Fundamentals Mathematics Algorithms Algebra
'''
def lost_sheep(friday,saturday,total):
    return total - sum(friday) - sum(saturday)

if __name__ == '__main__':
    print(lost_sheep([1,2],[3,4],15))
    print(lost_sheep([3,1,2],[4,5],21))
    print(lost_sheep([5,1,4],[5,4],29))