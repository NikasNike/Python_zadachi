from operator import index
from sys import api_version
import random
#Дан список чисел. Выделить среди них числа, удовлетворяющие условию: следующее больше предыдущего. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

mass = [1, 5, 2, 3, 4, 6, 1, 7, 9, 11]
#mass = [random.randint(1, 4) for _ in range(10)]
print(mass)
minIn = min(mass)

res = []

for i in mass:
    if minIn+1>i>minIn-1: 
        res.append(i)
        minIn += 1
    #дополнение +2 может перескакивать через 1 цифру
    elif minIn+2>i>minIn-1:
        res.append(i)
        minIn += 2
    #дополнение + 3 перескакивать через 2 цифры
#    elif minIn+3>i>minIn-1:
 #       res.append(i)
  #      minIn += 3
print(res)
        
#автоматизировть и сдлеать дополнения от того как скажет пользователь
#сделать цикл что бы он перебирал то значение которое я введу в прибавление к минимальному числу

