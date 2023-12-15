# Дано вещественное число — цена 1 кг конфет.
# Вывести стоимость 0.1, 0.2, ..., 1 кг конфет.

# запрашивем стоимость килограмма
price = input('Введите стоимость конфет за 1 кг: ')

# обработка исключений
while type(price) != int:
    try:
        price = int(price)
    except ValueError:
        print('Вы ввели не число!')
        price = input('Введите стоимость конфет за 1 кг: ')

step = 0.1  # шаг
i = 0.1  # счетчик

# считаем и выводим информацию о стоимости конфет при разном весе
while i <= 1:
    price_step = price * i
    i = round(i, 2)
    price_step = round(price_step, 2)
    print(f'Стоимость {i}кг конфет: {price_step}')
    i += step
