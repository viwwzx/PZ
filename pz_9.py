# Дан словарь с четным количеством элементов.
# Найти суммы значений элементов первой и второй половин
# с использованием функции. Результаты вывести на экран
even_dict = {1: 3, 2: 5, 3: 1, 4: 9}

def summa(x):
    first_half = sum(list(x.values())[:len(x)//2])
    second_half = sum(list(x.values())[len(x)//2:])
    return first_half, second_half

end1, end2 = summa(even_dict)
print(f'Сумма первой половины: {end1}\nСумма второй половины: {end2}')