#Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#ПО ВТОРОМУ ПРИМЕРУ
from msilib.schema import MsiAssembly
from random import randint
def fex(k):
    mass = []
    mass2 = []
    end = []
    index = 0
    
    for i in range(1, k+1):
        mass2.append(i)
        mass.append(randint(0, 100))

    for i in mass:
        if len(mass) > (index * -1) + 1 :
            a = str(f'{i} * x^{mass2[index-1]} + ')
            end.append(a)
            index -= 1
        elif len(mass) == index * -1 + 1:
            a = str(f'{i} = 0 ')
            end.append(a)
    
    for i in end:
        print(i, end = '')
    return end
    
fex(5)
