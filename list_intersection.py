def list_intersection(a: list, b: list):
    ''' Функция принимает массивы a и b 
        И возвращает пересечение этих массивов
    '''
    c = []
    for i in a:
        for n in b:
            if i == n:
                c.append(i)
                break
    return c


def test1_list_intersection():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4, 5]
    c = list_intersection(a, b)
    if c == [1, 2, 3, 4, 5]:
        print('test#1 is ok')
    else:
        print('test#1 is failed')


def test2_list_intersection():
    a = [1, 2, 3, 4, 5]
    b = []
    c = list_intersection(a, b)
    if c == []:
        print('test#2 is ok')
    else:
        print('test#2 is failed')


def test3_list_intersection():
    a = [1, 2, 3, 4, 5]
    b = [3, 4]
    c = list_intersection(a, b)
    if c == [3, 4]:
        print('test#1 is ok')
    else:
        print('test#1 is failed')


def test4_list_intersection():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    c = list_intersection(a, b)
    if c == []:
        print('test#1 is ok')
    else:
        print('test#1 is failed')


test1_list_intersection()
test2_list_intersection()
test3_list_intersection()
test4_list_intersection()
