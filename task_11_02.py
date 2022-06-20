# Создать собственный класс-исключение, для обработки ситуации
# деления на ноль и функцию, выполняющую деление двух чисел.

class ZeroOnNull(Exception):
    text = "Деление на ноль невозможно"

    def __str__(self):
        return self.text

def division(num1, num2):
    try:
        if num2 == 0:
            raise ZeroOnNull
        else:
            rez = num1 / num2
            return rez
    except ZeroOnNull as err:
        return err

print(division(26, 2))
print(division(10, 5))
print(division(10, 0))
