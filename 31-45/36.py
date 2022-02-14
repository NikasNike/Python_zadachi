#Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def miss(n):
    mass = []
    rev = 0
    for i in range(1, n+1):
        o = ((1**i + 1) **i)
        mass.append(round(o, 2))
        rev += mass[i-1]
    print(rev)
    print(mass)
miss(5)

