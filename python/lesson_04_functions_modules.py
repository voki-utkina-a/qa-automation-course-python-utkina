def summa(a, b):
    res = a + b
    print('result:', res)
summa(5, 7 )
summa('H', 'i')

def summa(a, b):
    return a + b
res = summa(10, 3)
print(res)

def summa(l):
    return sum(l)
num1 = [5, 1, 2, 3, 4]
print(summa(num1))

def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
            min_number = el
    print(min_number)
num1 = [5, 1, 2, 3, 4]
minimal(num1)
num2 = [5, 1, 0.22, 3, 0.214]
minimal(num2)

def maximum(l):
    max_num = l[0]
    for el in l:
        if el > max_num:
            max_num = el
    return(max_num)
num1 = [5, 10, 2, 3, 4]
print('maximum:', maximum(num1))

func = lambda x, y: x + y
res = func(7, 3)
print(res)

def check_test_status(status):
    if status == 'passed':
        return 'Test passed'
    else:
        return 'Test failed'
result = check_test_status('failed')
print(result)

import random
number = random.randint(1, 10)
print(number)

import datetime as d, sys, os, platform
print(d.datetime.now())
print(sys.path)
print(os.name)
print(platform.system())

from math import sqrt as s, ceil
print(ceil(s(100)))