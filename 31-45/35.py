#Написать программу получающую набор произведений чисел от 1 до N.

from functools import reduce

n = 5
sum = 1
li = [x for x in range(1, n+1)]
li = reduce(lambda sum, x:  sum * x,  li)
print(li)

