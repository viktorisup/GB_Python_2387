# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

import os

folder_lst = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in folder_lst:
    dir1 = os.path.join('.', i)
    if os.path.exists(dir1) is False:
        os.mkdir(dir1)