# Дан словарь с четным количеством элементов.
# Найти суммы значений элементов первой и второй половин
# с использованием функции. Результаты вывести на экран
even_dic = {1: 3, 2: 5, 3: 1, 4: 9}

first_half = sum(list(even_dic.values())[:len(even_dic)//2])
second_half = sum(list(even_dic.values())[len(even_dic)//2:])

print(first_half)
print(second_half)
