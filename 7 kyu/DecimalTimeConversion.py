'''
https://www.codewars.com/kata/6397b0d461067e0030d1315e/train/python

Decimal Time Conversion



Write two functions, one that converts standard time to decimal time and one that converts decimal time to standard time.

    One hour has 100 minutes (or 10,000 seconds) in decimal time, yet its duration is the same as in standard time. Thus a decimal minute consists of 36 standard seconds, which is 1/100 of an hour.
    Working time is usually rounded to integer decimal minutes. Thus one standard minute equals 0.02 decimal hours, while two standard minutes equal 0.03 decimal hours and so on.
    The terms "normal time" and "standard time" are considered synonymous in this kata.
    to_industrial(time) should accept either the time in minutes as an integer or a string of the format "h:mm". Minutes will always consist of two digits in the tests (e.g., "0:05"); hours can have more. Return a float that represents decimal hours (e.g. 1.75 for 1h 45m). Round to a precision of two decimal digits - do not simply truncate!
    to_normal(time) should accept a float representing decimal time in hours. Return a string that represents standard time in the format "h:mm".
    There will be no seconds in the tests. We'll neglect them for the purpose of this kata.


Flavor text (click to expand)
Calculations with time units can be confusing, because we are used to calculating in the decimal system in every day use. An hour, however, consists of sixty minutes, which in turn consist of sixty seconds each.

When dealing with multiple entries of measured time - for example, in a working time recording - it can get hard to correctly sum up the total. A seemingly natural algorithm is to add up hours and minutes separately, then divmod the minutes with 60 to get additional complete hours and remaining minutes.

In Germany, some companies use decimal time (in German: "Industriezeit" or "Industriestunden") to keep track of working hours, which makes it a lot easier to calculate multiple entries.

Examples:
to_industrial(1) => 0.02
to_industrial("1:45") => 1.75
to_normal(0.33) => "0:20"

Please leave a rating if you liked this kata!

Fundamentals Algorithms Date Time Strings
'''

def to_industrial(time):
    if isinstance(time, int) or isinstance(time, float):
        res = round(time / 60, 2)
    elif isinstance(time, str):
        hours, mins = [int(i) for i in time.split(':')]
        res = round((hours * 60 + mins) / 60, 2)
    return res


def to_normal(time):
    res = time * 60
    return f'{round(res // 60)}:{round(res % 60):02d}'


if __name__ == '__main__':
    print(to_industrial('1:45'))
    print(to_industrial(7))
    print(to_normal(12.07))
    print(to_normal(0.33))
