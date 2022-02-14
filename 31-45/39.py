
from random import randint, shuffle

#Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

mass = []
a = int(input("введите минимальное значение: "))
b = int(input("Введите максимально значение: "))
while a < b:
    mass.append(a)
    a += 1
shuffle(mass)
print(mass[1])
