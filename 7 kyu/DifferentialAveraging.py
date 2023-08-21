'''
https://www.codewars.com/kata/52c32ef251f31ae8f50000ae



Say you have a ratings system. People can rate a page, and the average is displayed on the page for everyone to see.

One way of storing such a running average is to keep the the current average as well as the total rating that all users have submitted and with how many people rated it, so that the average can be calculated and updated when a new rating has been made.

There are a couple of minor problems with this: first, you're keeping 3 columns instead of 1, which isn't ideal. Second is, if you're not careful, the number could get too large and get less and less accurate as the data format tries to keep up.

So what you need to do is this: write a function that takes the current average, the current number of ratings (data points) made, and a new value to add to the average; then return the new value. That way, you only need 2 columns in your database, and the number will not get crazy large over time.

To be clear:

current = 0.5
points = 2
add = 1

--> 0.6666666666666666666666666666666666 // (2/3)

There are also plenty of examples in the example tests.
'''
def add_to_average(current, points, add):
    return (current * points + add) / (points + 1)



if __name__ == '__main__':
    print(add_to_average(0,0,1))
    print(add_to_average(1,1,2))
    print(add_to_average(1.5,2,3))
    print(add_to_average(0,0,123))
    print(add_to_average(123,1,456))
    print(add_to_average(289.5,2,789))