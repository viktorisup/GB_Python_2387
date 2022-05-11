# Написать генератор нечётных чисел от 1 до n (включительно),
# без использования ключевого слова yield, полностью истощить генератор.

def iterator_without_yield(n):
    for num in range(n + 1):
        if num % 2 == 1:
            yield num

gen1 = iterator_without_yield(11)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))