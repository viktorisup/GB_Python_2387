# Усложнение [одна звездочка]:
# нужен генератор нечётных чисел от 1 до n (включительно), для чисел, квадрат которых меньше 200.
# Все остальное как в основном задании.

def iterator_without_yield(n):
    tmp = (num for num in range(1, n + 1, 2) if (num ** 2) < 200)
    return tmp

gen1 = iterator_without_yield(100)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
