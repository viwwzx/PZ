# Если в матрице имеются положительные элементы, то вывести TRUE,
# иначе FALSE

import random

matrix = [[random.randint(-7, 2) for i in range(3)] for j in range(3)]
print(matrix)

def trueorfalse(x):
    for i in x:
        for j in i:
            if j > 0:
                return True
    return False


print(trueorfalse(matrix))
