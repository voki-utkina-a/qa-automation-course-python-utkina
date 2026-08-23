def summa(a, b):
    res = a + b
    print('result:', res)
summa(5, 7 )
summa('H', 'i')


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