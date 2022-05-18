# Вывод на экран записей:
# Имя исполняемого скрипта: task_4_show_sales.py
# Предполагаем, что первая запись имеет номер 1.
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи от номера,
# равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная от номера,
# равного первому числу, по номер, равный второму числу, включительно;
# Если второе число больше, чем количество записей в файле - просто выводить до конца.
# Корректно обработать неправильное количество или тип переданных параметров.

import sys

with open('bakery.csv', 'rt', encoding='utf-8') as f:
    idx_line = f.readlines()
    if len(sys.argv) == 1:
        for i in idx_line:
            print(i.strip())
    elif len(sys.argv) == 2 and sys.argv[1].isdigit() and len(idx_line) > int(sys.argv[1]):
        idx_start = int(sys.argv[1])
        for i in idx_line[idx_start - 1:]:
            print(i.strip())
    elif len(sys.argv) == 3 and sys.argv[2].isdigit():
        idx_start = int(sys.argv[1])
        idx_end = int(sys.argv[2])
        for i in idx_line[idx_start - 1:idx_end]:
            print(i.strip())
    else:
        print('Неверные аргументы')



