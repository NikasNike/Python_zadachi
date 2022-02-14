#Выяснить, кратно ли число заданному, если нет, вывести остаток.
num = int(input('Ввести число: '))
num2 = int(input('Ввести число: '))



def func (num1, num2):
    return 'кратно' if num1%num2 == 0 else (f'остаток: {num1%num2}')
print(func(num, num2))
