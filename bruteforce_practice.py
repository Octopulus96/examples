#Bruteforce

def is_simple_number(x):
    """ Определяет, является ли чисор простым.
        x - целое число
        Если просто, то возвращает True,
        а иначе - False
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    ''' Раскладывает число на множители b .
        Печатает их на экране.
        x - целое положительное число
    '''
    divisor = 2
    massive = []
    while x > 1:
        if x % divisor == 0:
            x //= divisor
            massive.append(divisor)
        else:
            divisor += 1
    if massive == []:
        return None
    else:
        return massive
      