# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх заданных списков.

nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом', 'курица', 'дрозд', 'слон']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

from random import choice

def get_jokes(q, lst_1=['бабер'], lst_2=['пять секунд назад'], lst_3=['скучный']):
    """Функция случайным образом генерирует фразу-шутку"""
    lst_fun = []
    for i in range(q):
        rnd_1 = choice(lst_1)
        rnd_2 = choice(lst_2)
        rnd_3 = choice(lst_3)
        str_fun = ''
        str_fun += rnd_1 + ' ' + rnd_2 + ' ' + rnd_3
        lst_fun.append(str_fun)
    print(lst_fun)

get_jokes(3, nouns, adverbs, adjectives)