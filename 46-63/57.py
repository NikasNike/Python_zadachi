# 57.	Дан список чисел. Выделить среди них максимальное количество чисел, удовлетворяющих условию предыдущей задачи. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
init_lst = [1, 5, 2, 3, 4, 6, 1, 7]
result_list = []
len_lst = len(init_lst)

for item_index in range(len_lst):
    temp_list = [init_lst[item_index]] 
    result_list += [temp_list[:]]
    for sub_item_index in range(item_index + 1, len_lst):
        result_list += get_sub_list(sub_item_index, init_lst, temp_list[:])

print(result_list)
print(len(result_list))   
max_list = 0

save_i_list = []
for i_list in result_list:
    if len(i_list) > max_list:
        max_list = len(i_list)
        save_i_list = i_list
print(save_i_list)        

print(max(map(lambda x: len(x), [i_list for i_list in result_list])))