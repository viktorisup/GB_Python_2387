# Создать структуру файлов и папок, как написано в задании 2
# (при помощи скрипта или «руками» в проводнике). Написать скрипт,
# который собирает все шаблоны в одну папку templates:

import os, shutil

dir1 = os.path.join('..', 'templates')
if os.path.exists(dir1) is False:
    os.mkdir(dir1)

dirs_lst = []
for name, dirs, files in os.walk('.'):
    dirs_lst.append(name)

for i in dirs_lst:
    if i.find('templates') != -1:
        dir_tmp = i.split('templates')[0]
        dir_main = os.path.join(dir_tmp, 'templates')
        shutil.copytree(dir_main, dir1, dirs_exist_ok=True)
