
#Найти НОК двух чисел
a = int(6)
b = int(7)
i = a
for x in range(1, 10):
    if (i %b) ==0 and (i%a) == 0:
        print(i)
        break
    else:
        i += a

