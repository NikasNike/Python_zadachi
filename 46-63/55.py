#В файле находится N натуральных чисел, записанных через пробел.
#  Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его.

mass = [1, 2, 3, 4, 5, 6, 8, 9, 10 ]
index = len(mass)
ind = 1
for i in mass:
    if i +1 == mass[ind]:
        # print(i)
        ind += 1
    elif i + 1 != mass[ind]:
        mass.insert(i, i+1)
        ind += 1
        print(mass[i])
        break
print(mass)