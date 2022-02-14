#Определить, позицию второго вхождения строки в списке либо сообщить, что его нет.
lst = ['rysghif', 'hjfyrh', 'tyif']
lst2 = 'if'
index = 0
for i, item in enumerate(lst):
    pos = item.find(lst2)
    if pos != -1:
        index += 1
    if index == 2:
        print(f'{i+1} позиция в списке')
    if (i+1 >= len(lst)) and index < 2:
       print('NO')

