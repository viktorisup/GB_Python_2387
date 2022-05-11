# Есть два списка: tutors - имена учеников, groups - названия их классов.
# Необходимо реализовать генератор или функцию-генератор, возвращающий кортежи вида '(<tutor>, <group>)'.

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def gen_tuple(list_1, list_2):
    i = 0
    j = 0
    while i < len(list_2) or j < len(list_1):
        if j >= len(list_1):
            yield (None, list_2[j])
            i += 1
            j += 1
        elif i >= len(list_2):
            yield (list_1[i], None)
            i += 1
            j += 1
        else:
            yield (list_1[i], list_2[j])
            i += 1
            j += 1

gen_1 = gen_tuple(tutors, groups)

print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
print(next(gen_1))
