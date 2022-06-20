import sys
import os

rate_val = 10 # Кратность
range_val = 5 # Диапазон
rate_lst = []
for i in range(0, range_val):
    if rate_val * (rate_val ** i) == 1:
        rate_lst.append(i)
    else:
        i1 = rate_val * (rate_val ** i)
        rate_lst.append(i1)

size = {}
size_lst = []
count = 0
with os.scandir('some_data') as f:
    for i in f:
        j = i.path
        j1 = os.path.getsize(j)
        size_lst.append(j1)

for i in rate_lst:
    for j in size_lst:
        if int(i) >= int(j):
            count += 1
            size.update({i : count})
    count = 0

print(size)