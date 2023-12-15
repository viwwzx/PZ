# Дан список размера N. Переставить в обратном порядке
# элементы списка, расположенные между его минимальным
# и максимальным элементами, включая минимальный
# и максимальный элементы.

import random

# создаем функцию, в котором работаем со списком и его мин и макс
def reverse_spisok(n):
    spisok = (random.sample(range(15), n))

    n1 = min(spisok)
    n2 = max(spisok)

    n1_id = spisok.index(n1)
    n2_id = spisok.index(n2)

    n1_id, n2_id = min(n1_id, n2_id), max(n1_id, n2_id)

    rev_spisok = spisok[0:n1_id]+spisok[n1_id:n2_id+1][::-1]+spisok[n2_id+1:]

    return f'Изначальный список: {spisok}\nМинимум и максимум: {n1} {n2} \nПеревернутый список: {rev_spisok}'

# запрашиваем число и выводим списки и мин макс
print(reverse_spisok(int(input('Введите размер списка: '))))

