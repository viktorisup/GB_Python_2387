# Реализовать класс «Дата».

from datetime import date as D

date_lst = []
class Date:
    def __init__(self, date = date_lst):
        self.date = date

    @classmethod
    def func1(cls, date):
        date_lst.clear()
        try:
            for i in date.split('-'):
                date_lst.append(i)
            return int(date_lst[0]), int(date_lst[1]), int(date_lst[2])
        except Exception:
            print('DateInitError: Не возможно извлеч дату')

    @staticmethod
    def valid(date = date_lst):
        try:
            day, month, year = date
            D(int(year), int(month), int(day))
            return True
        except Exception:
            print(f'{date} Неверный формат даты')
            return False

    def __str__(self):
        try:
            day, month, year = date_lst
            return f'Дата {year}.{month}.{day}'
        except Exception:
            print(f'Дата {self.date}: Не возможно напечатать дату')

print(Date.func1('31-12-2021'))
print(Date.valid())
d1 = Date.func1('31-12-2021')
print(Date())

print(Date.func1('32-12-2022'))
print(Date.valid())
d2 = Date.func1('32-12-2022')
print(Date())

print(Date.func1('12-12--2022'))
print(Date.valid())
d3 = Date.func1('12-12--2022')
# print(Date('12-12--2022'))