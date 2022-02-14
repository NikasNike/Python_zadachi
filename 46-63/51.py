#Составить список простых множителей натурального числа N
n = 3050
mass = []
#while n <= 0:
index = 0
fio = 0
while n != 1:
    for i in range(-9, -1):
        i = i * -1
        if i == 2:
            fio += 1
        if n % i == 0:
            n = n / i
            mass.append(i)
            index += 1 
            
        elif fio > index:
            mass.append(n)
            n = n / n
print(mass)