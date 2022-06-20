# Реализовать класс Road (дорога).

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def massa_asp(self):
        massa = self._length * self._width * 25 * 5
        print(f'{self._width}м*{self._length}м*{25}кг*{5}см = {massa/1000:.0f}')


a = Road(5000, 20)
a.massa_asp()
