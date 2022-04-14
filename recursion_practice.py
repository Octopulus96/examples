''' Рекурсия обязательно иммет
    1) рекуррентный случай
    2) крайний случай
'''

''' Факториал'''
def f(n: int):
    assert n >= 0, "Факториал отрицательного не определен"
    if n == 0:
        return 1
    return f(n - 1) * n

''' Алгоритм Евклида'''  
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

''' Быстрое возведение в степень'''
def pow(a: float, n: int):
    if n == 0:
        return 1
    elif n%2 == 1:
        return pow(a, n-1) * a
    else:
        return pow(a**2, n//2)

''' Ханойские башни'''

def matryoshka(n):
    if n == 1:
        print("Матрёшечка")
    else:
        print("Верх матрёшка n=", n)
        matryoshka(n-1)
        print("Низ матрёшки n=", n)

def sand_clock(n: int):
    ''' Выводит в командной строке песочные часы,
        высотой равной n.
    '''
    t = 0
    if n == 1:
        print(" " * t,("|" * n)*2)
    else:
        print(" " * t,("|" * n)*2)
        sand_clock(n-1, t+1)
        print(" " * t,("|" * n)*2)
