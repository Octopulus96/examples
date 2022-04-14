''' List comprehensions'''
A = [x ** 2 for x in range (10)]
# Эквивалентно
A = []
for x in range(10):
    A.append(x ** 2)

''' Необходимо создать новый список на основе A,
    в котором все числа четные,
    а отрицательные числа заменить на 0'''
A = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]

B = [0 if x < 0 else x for x in A if x % 2 == 0]
# Эквивалентно
B = []
for x in A:
    if x%2 == 0:
        if x < 0:
            B.append(0)
        else:
            B.append(x)
