# Дан список, содержащий искаженные данные с должностями и именами сотрудников:
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита'].
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'

lst_1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']


for i in lst_1:
    new_lst = i.split()
    name = str(new_lst[-1]).capitalize()
    prof_x = new_lst[:-1]
    prof = ' '.join(prof_x)
    print(f'Привет, {prof} {name}!')

