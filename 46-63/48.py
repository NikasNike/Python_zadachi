import math
#Найти корни квадратного уравнения Ax² + Bx + C = 0

a = 1
b = 6
c = 9

D = math.pow(b,2) + (4*a*c)
print(D)

if D ==0: print(f'Корень равен {-b / 2*a}')
if D < 0: print('Нет корней')
if D > 0:
    k1 = (-b - (D/2)) / (2*a)
    k2 = (-b + (D/2)) / (2*a)
    print(k1, k2)
