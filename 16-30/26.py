 #Возведите число А в натуральную степень B используя цикл

def niss(a, b):
    for i in range(1, b+1):
        print(f'Число {a} в степени {i} = {a**i}')
niss(2, 4)
