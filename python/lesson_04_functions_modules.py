def summa(a, b):
    res = a + b
    print('result:', res)
summa(5, 7 )
summa('H', 'i')

def summa(a, b):
    return a + b
res = summa(10, 3)
print(res)

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

func = lambda x, y: x + y
res = func(7, 3)
print(res)

import random
number = random.randint(1, 10)
print(number)

def check_test_status(status):
    if status == 'passed':
        return 'Test passed'
    else:
        return 'Test failed'
result = check_test_status('failed')
print(result)