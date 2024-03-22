# В последовательности на n целых чисел умножить элементы до n-1
# на элемент n

n = 5

newlist = [x for x in range(1, n + 1)]
listmult = [x * n for x in newlist[0:4]]
listmult.append(newlist[4])

print(newlist, listmult)
