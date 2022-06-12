# Создайте собственный класс-исключение, используемый
# для проверки содержимого списка на наличие только чисел.

class Error(Exception):
    def __init__(self, text = 'Неверный формат введеных данных'):
        self.text = text

    def __str__(self):
        return self.text

lst1 = []

while True:
    user_data = input("Введите число или 'stop' для выхода: ")

    if user_data == "stop" or user_data == '':
        break
    try:
        if not user_data.isdigit():
            raise Error
        lst1.append(int(user_data))
    except Error as err:
        print(err)

print(lst1)