#Написать программу преобразования десятичного числа в двоичное
num1 = 5986 #число в десятичной системе
sistem = 8 # система в которую надо возвести число

num2 = []

while num1 > 0:
    if num1 == 0:
        print(num2)
        break
    else:
        if num1%sistem ==0: 
            num2.append(0)
            num1 /= sistem
        else:   
            g = num1%sistem
            num2.append(g)
            num1 -= g
            num1 /= sistem
print(num2) #читается в право на лево