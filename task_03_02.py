# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имен, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*args):
    dict_name = {}
    for name in args:
        key = name[0].title()
        if key in dict_name:
            dict_name[key].append(name)
        else:
            dict_name[key] = [name]
    return dict_name

print(thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Артем', 'Вадим', 'Анатолий', 'Виталий', 'Макс'))
