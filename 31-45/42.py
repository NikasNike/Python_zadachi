# сумма чисел на нечетной позиции

import random

a=[random.randint(-10, 10) for _ in range(9)]
print(a)
res = 0
for i, number in enumerate(a):
    if i%2 != 0:
        res += number
print(res)