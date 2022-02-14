#Даны два числа. Показать большее и меньшее число


number  = int(input('Введите число>>' ))
number2  = int(input('Введите число 2>>' ))
if number > number2:
    print( number)   
elif number2 > number:
    print( number2)
elif number2 == number:
    print("одинаковые числа")
else:
    print('неверное значение')

