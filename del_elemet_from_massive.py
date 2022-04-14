def del_odd_numbers(massive:list):
    '''Удаление четных чисел из массива'''
    for number in massive:
        if number % 2 == 0:
            massive.remove(number)


def del_even_numbers(massive:list):
    '''Удаление нечетных чисел из массива'''
    for number in massive:
        if number % 1 == 0:
            massive.remove(number)


def del_simbols(massive:list):
    '''Удаление символов из массива'''
    for elements in massive:
        if elements == str:
            massive.remove(elements)

