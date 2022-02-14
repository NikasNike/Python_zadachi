
#Вычислить число  c заданной точностью d
#	Пример: при d = 0.001, π = 3.141. 10-1≤d≤10-10
import math
d = "0.0000000000000000001"
d = int(len(d) - 2)
pi = round(math.pi, d)
print(pi)
print('{:.20}'.format(math.pi))#вместо цифра  не ставится D


