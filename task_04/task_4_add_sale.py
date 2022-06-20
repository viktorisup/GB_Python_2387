# Запись в файл новых данных:
# Имя исполняемого скрипта: task_4_add_sale.py
# При записи передавать из командной строки значение суммы продаж.
# Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.

import sys

if len(sys.argv) == 1:
    print('Количество аргументов должно быть два')
elif len(sys.argv) == 2 and sys.argv[1].isdigit():
    with open('bakery.csv', 'at', encoding='utf-8') as f:
        f.write(f'{sys.argv[1]}\n')
else:
    print('Передайте два аргумента, второй аргумент должен быть числом')