#По двум заданным числам проверять является ли одно квадратом другого
def met (num, num2):
    if num**2 == num2 :
        print(f'число {num} квадрат {num2}')
    elif num2**2 == num:
        print(f'квадрат {num} числа {num2}')
    else:
        print('неа')
met(100,10)
    
    