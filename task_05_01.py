# Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор.

def iterator_without_yield(n):
    tmp = (num for num in range(n + 1) if num % 2 == 1)
    return tmp

gen1 = iterator_without_yield(11)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))