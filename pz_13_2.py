# Если в матрице имеются положительные элементы, то вывести TRUE,
# иначе FALSE

matrix = [[-7, -8, -9], [-4, 2, -6], [-7, -8, -9]]


def trueorfalse(x):
    for i in x:
        for j in i:
            if j > 0:
                return True
    return False


print(trueorfalse(matrix))
