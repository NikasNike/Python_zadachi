#Строка содержит набор чисел. Показать большее и меньшее число
from operator import index
from re import A
#РАБОТАЕТ ОТ 0 до 99


num1 = []
sum_num_str = ' '
item_num = 0
indeX = 0
stop = 0



path = 'C:/Users/nikas/Desktop/PHYTHON/Python_zadachi/io.txt'
data = open(path, 'r')
for line in data:
    a =(line)



for i in a:
    if stop == 1:
        break
    elif i == a[indeX]:

        if i != ' ':
            while a[indeX] != ' ':
                num_str = str(a[indeX])
                item_num += 1
                sum_num_str = sum_num_str + num_str
                if indeX < len(a)- 1:
                    indeX += 1
                else:
                    num1.append(int(sum_num_str))
                    stop += 1
                    break
            else:
                num1.append(int(sum_num_str))
                num_str = ''
                if item_num >= 2:
                    indeX += 1
                indeX -= item_num
                item_num = 0
                sum_num_str = ' '
        if indeX < len(a)- 1:
            indeX += 1
print(num1)

## РАБОТАЕТ С ЛЮБЫМИ ЦИФРАМИ и с множеством пробелов НО не со знаками  
        

















#####################мое
# for i in a:
#     if i == a[index]:
#         if i == ' ':
#             index += 1
#         elif index+1 == len(a):
#             mass.append(i)
#         elif index != len(a):
#             if i != ' ' and a[index+1] == ' ':
#                 mass.append(i)
#                 index += 1
#             elif a != ' ' and a[index+1] != ' ':
#                 mass.append(i+a[index+1])
#                 index += 2
# for num in mass:
#     num1.append(int(num))


# print(num1)
# maxIn = max(num1)
# minIn = min(num1)
# print(minIn, maxIn)
###################################не мое
# def larger_and_smaller_numbers_in_row(row_number):
#     number_list = []
#     for i in row_number:
#         int_s = int(i)
#         number_list.append(int_s)
#     max_N = max(number_list)
#     min_N = min(number_list)
#     return max_N, min_N
# set_numbers = input('Введите подряд нескольно чисел: ')
# more, less = larger_and_smaller_numbers_in_row(set_numbers)
# print(f'max - {more}, min - {less}')