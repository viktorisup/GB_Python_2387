# Реализовать проект «Операции с комплексными числами».

class ComplexNum:
    def __init__(self, real, imag):
        self.complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, ComplexNum):
            other = other.complex

        complex1 = self.complex + other
        return ComplexNum(complex1.real, int(complex1.imag))

    def __sub__(self, other):
        if isinstance(other, ComplexNum):
            other = other.complex

        complex1 = self.complex - other
        return ComplexNum(complex1.real, int(complex1.imag))

    def __mul__(self, other):
        if isinstance(other, ComplexNum):
            other = other.complex

        complex1 = self.complex * other
        return ComplexNum(complex1.real, int(complex1.imag))

    def __str__(self):
        return self.complex.__str__()

c1 = ComplexNum(2, 3)
c2 = ComplexNum(-1, 1)
print(c1)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)

