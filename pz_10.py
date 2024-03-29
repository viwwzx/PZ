# Книжные машазины предлагают следующие коллекции книг.
# Определить в каких магазинах можно приобрести книги Маяковского.

# записываем множества
magister = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domKnigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bookMarket = {'Пушкин', 'Достоевский', 'Маяковский'}
gallery = {'Чехов', 'Тютчев', 'Пушкин'}

# создаем список с множествами, для того чтобы обращаться по индексу
spisok = [magister, domKnigi, bookMarket, gallery]

# создаем еще список, с теми же элементами в том же порядке,
# но в строчном виде, чтобы вывести в ответе
spisokName = ['Магистр', 'Дом книги', 'Бук маркет', 'Галерея']

# создаем множество для поиска общего элемента
word = {'Маяковский'}

# находим количество множеств(магазинов), чтобы не считать ручками
lenSpisok = len(spisok)

# ищем общее значение, сравниваем с искомым и выводим результат
for i in range(0, lenSpisok, +1):
    if word & spisok[i] == word:
        print(f'Книги Маяковского можно приобрести в магазине: {spisokName[i]}')
