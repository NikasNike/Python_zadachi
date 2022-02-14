#Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
#Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
lst =[1, 2, 3, 5, 1, 5, 3, 10, 11]
dct = dict.fromkeys(lst, 0)
print(dct)
for item in lst:
    dct[item] += 1

print([index for index, value in dct.items() if value == 1])


