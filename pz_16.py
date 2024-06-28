#Создайте класс "Календарь", который имеет атрибуты год, месяц и день
#Добавьте методы для определения дня недели, проверки на високосный год
#и определения количества дней в месяце

import datetime

class calendar:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def weekday(self):
        data = datetime.date(self.year, self.month, self.day)
        return data.strftime("%A")

    def visokosny(self):
        return self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0)

    def day_in_month(self):
        day_in_month = [31, 28 + self.visokosny(), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return day_in_month[self.month - 1]

calendar = calendar(2024, 6, 7)
print("День недели:", calendar.weekday())
print("Високосный год:", calendar.visokosny())
print("Количество дней в месяце:", calendar.day_in_month())
