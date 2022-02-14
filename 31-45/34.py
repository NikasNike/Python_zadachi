from tokenize import Double

#Подсчитать сумму цифр в вещественном числе.

num = str(111.19)
num = num.replace('.', '0')

rev = 0
for i in num: rev += int(i)
print(rev)


