#Задать номер четверти, показать диапазоны для возможных координат
x = int(input('Ввести число: '))
y = int(input('Ввести число: '))
if (x>0) & (y>0):
    print('Координаты в 1 четверти  ' )
elif (x<0) & (y>0):
    print('Координаты во 2 четверти ' )
elif (x<0) & (y<0):
    print('Координаты в 3 четверти  ' )
elif (x>0) & (y<0):
    print('Координаты в 4 четверти  ' )
elif (x==0) & (y==0):
    print('КООРДИНАТЫ РАВНЫ 0  ' )
elif (x==0) | (y==0):
    print('КООРДИНАТЫ ЛЕЖАТ НА ЛИНИИ ФУНКЦИИ, а на какой мне лень писать ' )
else:
    print('хз')