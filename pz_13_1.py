#В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза
import random

matrix = [[random.randint(1, 5) for i in range(3)] for j in range(3)]
print(*matrix)

newmatrix = matrix

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if j!=i:
            newmatrix[i][j] = matrix[i][j]*2


#matrix = [[i for i in matrix[0]] for j in matrix] #не понимаю как добавить if и проблема с индексом

print(*newmatrix)
