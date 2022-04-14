
#Копирование масива
def coppy_aray(massive:list):
    ''' Возвращает новый скопированый массив'''
    new_massive = [0] * len(massive)
    for index in range(len(massive)):
        new_massive[index] = massive[index]
    return new_massive


#Линейный поиск масива
def array_search(massive:list, long:int, x:int):
    ''' Осуществляет поиск числа x в масиве massive
        от 0 до long - 1 индекса включительно.
        Возвращает индекс элемента x в масиве.
        Или -1, если такого нет.
        Если в массиве несколько одинаковых элементов,
        равных x, то вернуть индекс первого по счёту.
    '''
    try:
        for index in range(long):
            if massive[index] == x:
                return index
        return -1
    except IndexError:
        return 0


#Обращение масива
def invert_array(massive:list, long:int):
    ''' Обращение массива (поворот задом-наперед)
        в рамках индексов от 0 до long-1
    '''
    try:    
        for index in range(long//2):
            massive[index], massive[long-1-index] = massive[long-1-index], massive[index]
        return massive
    except IndexError:
        return 0
