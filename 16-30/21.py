#Программа проверяет пятизначное число на палиндромом
num = int(input('Ввести число: '))
num1 = num / 10000 // 1
num2 = num / 1000 % 10 // 1
num4 = num / 10 % 10 // 1
num5 = num % 10 // 1
if (num1 == num5) & (num2 == num4):
    print('число полиграм')
else:
    print('не полиграм')