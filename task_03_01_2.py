# Написать функцию num_translate_adv, которая корректно обработает числительные, 
# начинающиеся с заглавной буквы. Если перевод сделать невозможно, вернуть объект None.

def num_translate_adv(key):
    x = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'черыре',
         'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь',
         'nine': 'девять', 'ten': 'десять'}
    if key.istitle() is True:
        key = key.lower()
        return x.get(key).capitalize()
    else:
        return x.get(key)


print(num_translate_adv('three'))
print(num_translate_adv('Four'))
print(num_translate_adv('Nine'))
print(num_translate_adv('six'))