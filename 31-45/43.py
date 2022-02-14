#Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
mass = [2, 6, 7, 5, 6]
dlin = int(len(mass) / 2)

mass1 = []
index = 1
for i in range(1, dlin+1):
    mass1.append(mass[index - 1] * mass[index * -1])
    index += 1
    if mass[index] == mass[index * -1 + -1]:
        mass1.append(mass[index] * mass[index])

print(mass1)

