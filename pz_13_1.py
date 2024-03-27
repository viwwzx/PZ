#В квадратной матрице все элементы, не лежащие на главной диагонали
# увеличить в 2 раза

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
newmatrix = matrix
lenline = len(matrix)
lencol = len(matrix[0])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if (i==0) and (j!=0) or (i==1) and (j!=1) or (i==2) and (j!=2):
            newmatrix[i][j] = matrix[i][j]*2

print(newmatrix)
