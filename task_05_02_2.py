# Усложнение [одна звездочка]:
# С ключевым словом yield - как в задании 1: генератор нечётных чисел
# от 1 до n (включительно), для чисел, квадрат которых меньше 200.

def iterator_without_yield(n):
    for num in range(1, n + 1, 2):
        if num ** 2 <= 200 :
            yield num

gen1 = iterator_without_yield(16)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))