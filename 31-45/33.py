#Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

from itertools import count

s_1 = input('Введите любое предложение: ')
s_2 = input('Введите еще раз любое предложение: ')
print(s_1.count(s_2))



