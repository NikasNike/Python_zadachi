# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

from functools import reduce
from random import random
import random
def mass(x):
    sum = 1
    with open('C:/Users/nikas/Desktop/PHYTHON/Python_zadachi/slovo.txt', 'r') as data:
        a=[random.randint(-10, 10) for _ in range(x)]
        print(a)
        for line in data:
            i = int(line)
            sum *= a[i-1]
                           
            print(f'Позиция: {i}')
        print(f'сумма: {sum}')
mass(10) 
#reduce(lambda data, a:data * a[data-1], data)

