# Реализовать проект расчёта суммарного расхода ткани на производство одежды.

from abc import ABC, abstractmethod

class AbstractTextil(ABC):

    @property
    @abstractmethod
    def coat_calc(self):
        pass

    @property
    @abstractmethod
    def costume_calc(self):
        pass

    @abstractmethod
    def add_to_reserve(self):
        pass

class Textil(AbstractTextil):
    _cloth = []
    def __init__(self, param):
        self.param = param
        self._cloth.append(self)

    def coat_calc(self):
        pass

    def costume_calc(self):
        pass

    def add_to_reserve(self):
        pass

class Coat(Textil):

    @property
    def coat_calc(self):
        return self.param / 6.5 + 0.5

    def add_to_reserve(self):
        x = 0
        for i in self._cloth:
            if isinstance(i, Coat):
                x += i.coat_calc
        return x

class Costume(Textil):
    @property
    def costume_calc(self):
        return 2 * self.param + 0.3

    def add_to_reserve(self):
        x = 0
        for i in self._cloth:
            if isinstance(i, Costume):
                x += i.costume_calc
        return x

c1 = Coat(12)
c2 = Coat(1)
c3 = Coat(121)
print(c1.coat_calc)
print(c2.coat_calc)
print(c3.coat_calc)
print(f'Общие затраты ткани на все пальто: {c3.add_to_reserve()}')

cs1 = Costume(15)
cs2 = Costume(8)
cs3 = Costume(22)
print(cs1.costume_calc)
print(cs2.costume_calc)
print(cs3.costume_calc)
print(f'Общие затраты ткани на все костюмы: {cs3.add_to_reserve()}')
