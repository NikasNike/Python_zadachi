
#Определить, присутствует ли в заданном списке строк, некоторое число 

lst = ['wejkrjkwerh dgff', 'wersdfgkjdj23365', 'sdf4fjdgfgg', 'fdgdgdfg3']
number = 8
print('да') if sum([str(number) in item for item in lst]) else print('нет')


