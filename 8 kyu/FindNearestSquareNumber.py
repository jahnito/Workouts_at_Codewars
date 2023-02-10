'''
https://www.codewars.com/kata/5a805d8cafa10f8b930005ba

Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)
'''


def nearest_sq(n):
    c = 1
    l = 0
    r = 0
    while True:
        i = c ** 2
        if i == n:
            return n
        elif i < n:
            l = i
        elif i > n:
            r = i
            break
        c += 1
    if n - l < r - n:
        return l
    else:
        return r


if __name__ == '__main__':
    print(nearest_sq(110))