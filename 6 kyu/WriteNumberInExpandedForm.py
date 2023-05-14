'''
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.

https://www.codewars.com/kata/5842df8ccbd22792a4000245/python
'''

def expanded_form(num):
    result = []
    digits = 0
    while num:
        k = (num % 10) * 10 ** digits
        digits += 1
        num //=10
        if k:
            result.append(k)
    result.sort(reverse=True)
    return ' + '.join([str(i) for i in result])



if __name__ == '__main__':
    print(expanded_form(120012))