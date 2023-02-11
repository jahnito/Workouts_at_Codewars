'''
https://www.codewars.com/kata/55c28f7304e3eaebef0000da

Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!


def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res
'''

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res.append(i)
        i += 1
    return res


if __name__ == '__main__':
    print(create_array(10))
