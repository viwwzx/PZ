#В исходном текстовом файле (hotline.txt) после фразы "Горячая линия"
#добавить фразу "Министерства образования Ростовской области",
#посчитать количество произведенных добавлений. Сколько номеров
#телефонов заканчивается на "03", "50". ВЫвести номера телефонов
#горячих линий, связанных с ЕГЭ/ГИА

import re

data = ''
with open('hotline.txt', 'r', encoding='UTF-8') as f:
    data = f.read()


with open('hotline_ed.txt', 'w', encoding='UTF-8') as file:
    patternAdd = 'Горячая линия'
    replacment = 'Горячая линия Министерства образования Ростовской области'
    result = re.sub(patternAdd, replacment, data)
    file.write(result)


matchesAdd = len(re.findall(patternAdd, data))
print('Добавлено:', matchesAdd)

patternNum03 = r"\B03"
matchesNum03 = len(re.findall(patternNum03, data))
print('Номеров, которые заканчиваются на 03:', matchesNum03)

patternNum50 = r"\B50"
matchesNum50 = len(re.findall(patternNum50, data))
print('Номеров, которые заканчиваются на 50:', matchesNum50)

patternEx = r"(?:ЕГЭ).+\b"
matchesEx = re.findall(patternEx, data)
print('Номера ЕГЭ:', matchesEx[0][-11:], matchesEx[1][-11:])

