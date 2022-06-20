# Реализовать программу работы с органическими клетками, состоящими из ячеек.

class Cells:
    def __init__(self, count):
        self.count = int(count)

    def __str__(self):
        return self.count * "*"

    def __add__(self, other):
        return Cells(self.count + other.count)

    def __sub__(self, other):
        x = self.count - other.count
        if x > 0:
            return Cells(x)
        else:
            raise ValueError('Результат вычисления отрицательный')

    def __mul__(self, other):
        return Cells(self.count * other.count)

    def __floordiv__(self, other):
        return Cells(self.count // other.count)

    def make_order(self, row):
        row_lst = ''
        y = self.count // row
        for i in range(y):
            row_lst += '*' * row + '\\n'
        row_lst += "*" * (self.count % row)
        return row_lst

c1 = Cells(5)
c2 = Cells(10)
c3 = Cells(16)
c4 = Cells(20)
c5 = Cells(25)
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print('Орефметические операции')
print(c1 + c2)
print(c3 - c2)
print(c1 * c2)
print(c5 // c2)
print(c3.make_order(5))
