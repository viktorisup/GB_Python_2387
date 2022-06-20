# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Загрузить данные из обоих файлов и сформировать словарь: ключи — ФИО,
# значения — данные о хобби. Сохранить словарь в текстовый файл. Проверить сохранённые данные.

import json

dict_result = {}
with open('users.csv', mode='rt', encoding='utf-8') as file:
    user_lst = []
    for line in file:
        u = line.strip().split(',')
        key = u[0][0]+u[1][0]+u[2][0]
        user_lst.append(key)
with open('hobby.csv', mode='rt', encoding='utf-8') as file1:
    hobby_lst = []
    for line1 in file1:
        h = line1.strip().replace(',', ';')
        hobby_lst.append(h)
i = 0
while i < len(user_lst) or i < len(hobby_lst):
    if i >= len(hobby_lst):
        dict_result.update({user_lst[i]:None})
    elif i >= len(user_lst):
        dict_result = dict(zip(user_lst, hobby_lst))
        print(dict_result)
        exit(1)
    else:
        dict_result.update({user_lst[i]: hobby_lst[i]})
    i+=1

print(dict_result)
with open('my_json.json', 'wt') as f:
    f.write(json.dumps(dict_result, ensure_ascii=False))