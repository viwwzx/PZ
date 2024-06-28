#Приложение БИБЛИОТЕКА для автоматизированного контроля литературных
#источников в библиотеке. БД должна содержать таблицу Каталог с информацией
#о книгах и следующей структурой записи: Код книги, Жанр, Страна издания,
#Серия, Автор, Название книги, Год выпуска, Анотация

import sqlite3 as sq

book_info = [
    (1, 'роман-эпопея', 'Россия', 'война и мир', 'лев николаевич толстой', 'война и мир', 1865, 'описывает русское общество в эпоху войны'),
    (5, 'роман', 'Россия', 'мастер и маргарита', 'михаил булгаков', 'мастер и маргарита', 1966, 'самый известный и неоднозначный роман 20 века'),
    (15, 'драма', 'Россия', 'на дне', 'максим горький', 'на дне', 1902, 'изображает группу обитателей ночлежного дома для неимущих')
]

with sq.connect('library.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS catalog")
    cur.execute("""CREATE TABLE IF NOT EXISTS catalog (
    book_id integer primary key autoincrement,
    genre text not null,
    country_pub text not null,
    series text not null,
    author text not null,
    title text not null,
    years integer not null,
    annotation text not null
    )""")

    #заполняем таблицу значениями из переменной
    cur.executemany("INSERT INTO catalog VALUES (?, ?, ?, ?, ?, ?, ?, ?)", book_info)

    #делаем выборку, сортировку по году издания и выводим
    cur.execute("SELECT book_id, title, years from catalog WHERE years > 1850 ORDER BY years")
    for result in cur:
        print(*result, sep=', ')

    print('')

    #выборка между числами по book_id и выводим
    cur.execute("SELECT book_id, title FROM catalog WHERE book_id BETWEEN 2 AND 7")
    for result in cur:
        print(*result, sep=', ')

    print('')

    #выборка от числа по book_id и выводим
    cur.execute("SELECT book_id, title FROM catalog WHERE book_id > 10")
    for result in cur:
        print(*result, sep=', ')

    print('')

    #обновляем значения
    cur.execute("UPDATE catalog SET years=1 WHERE author='михаил булгаков'")
    cur.execute("UPDATE catalog SET years=2 WHERE author='лев николаевич толстой'")
    cur.execute("UPDATE catalog SET years=3, book_id=70 WHERE author='максим горький'")
    cur.execute("SELECT book_id, author, years FROM catalog")
    for result in cur:
        print(*result, sep=', ')

    print('')

    cur.execute("DELETE FROM catalog WHERE book_id=5")
    cur.execute("SELECT * FROM catalog")
    for result in cur:
        print(*result, sep=', ')


#select update delete