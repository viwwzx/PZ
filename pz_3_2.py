# Составить программу, определяющую название цвета
# в зависимости от введенной длины волны

# просим длину волны
wave = input('Введите длину волны: ')

# обработка исключений
while type(wave) != int:
    try:
        wave = int(wave)
    except ValueError:
        print('Вы ввели не число!')
        wave = input('Введите длину волны: ')

# проверка условий и вывод
if wave<450: print('Это фиолетовый цвет')
if wave>450 and wave<480: print('Это синий цвет')
if wave>480 and wave<510: print('Это бирюзовый цвет')
if wave>510 and wave<550: print('Это зеленый цвет')
if wave>550 and wave<570: print('Это салатный цвет')
if wave>570 and wave<590: print('Это желтый цвет')
if wave>590 and wave<630: print('Это оранжевый цвет')
if wave>630: print('красный')