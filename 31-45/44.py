#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным 
# значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
lst = [1.1, 10.01, 5.9, 8.4]
float_lst =  [item % 1 for item in lst] #%1 убирает целое значение
print(float_lst)
print(f'{max(float_lst) - min(float_lst) : .2f}')
