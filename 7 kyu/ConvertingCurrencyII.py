'''
https://www.codewars.com/kata/5c744111cb0cdd3206f96665

Converting Currency II

Description:

Given the current exchange rate between the USD and the EUR is 1.1363636 write a function that will accept the Curency type to be returned and a list of the amounts that need to be converted.

Don't forget this is a currency so the result will need to be rounded to the second decimal.

'USD' Return format should be '$100,000.00'

'EUR' Return format for this kata should be '100,000.00€'

to_currency is a string with values 'USD','EUR' , values_list is a list of floats

solution(to_currency,values)

#EXAMPLES:

solution('USD',[1394.0, 250.85, 721.3, 911.25, 1170.67]) 
= ['$1,584.09', '$285.06', '$819.66', '$1,035.51', '$1,330.31']

solution('EUR',[109.45, 640.31, 1310.99, 669.51, 415.54]) 
= ['96.32€', '563.47€', '1,153.67€', '589.17€', '365.68€']

Lists Mathematics Fundamentals Algorithms Algebra Strings
'''

def solution(to_cur,value):
    exchange = 1.1363636
    if to_cur == 'USD':
        res = map(lambda x: '${0:,.2f}'.format(round(x * exchange, 2)), value)
    else:
        res = map(lambda x: '{0:,.2f}€'.format(round(x / exchange, 2)), value)
    return list(res)

if __name__ == '__main__':
    print(solution('USD',[1.01, 83.29, 5.0, 23.23, 724.22]))
    print(solution('EUR',[109.45, 640.31, 1310.99, 669.51, 415.54]))
