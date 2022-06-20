# Усложнение [две звездочки]: С ключевым словом yield: Вычислять и возвращает
# само число и накопительную сумму этого и предыдущих чисел.

def iterator_without_yield(n):
    num_tmp = 0
    for num in range(1, n + 1, 2):
        num_tmp += num
        yield (num, num_tmp)
    num_tmp + num

gen1 = iterator_without_yield(16)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))