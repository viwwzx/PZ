# Составить генератор(yield), который выводит из строки только буквы

def only_letters(x):
    yield from [i for i in x if i.isalpha()]


x = '123lama123mama123a4'
letters = only_letters(x)

for j in letters:
    print(j)
