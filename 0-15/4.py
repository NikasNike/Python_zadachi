# max из 3х
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите тертье число: '))
max = a
max = b if max < b else max
max = c if max < c else max
print(max)
