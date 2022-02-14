# 62.	Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.

# from winreg import ConnectRegistry


def set_archive(data, path):
    str2= ''
    i = 0
    sub_str = data[0]
    for char in data:    
        if sub_str == char:
            i += 1
            continue
        str2 += str(i) + sub_str
        sub_str = char
        i = 1
    str2 += str(i) + sub_str    
    with open(path, 'w') as file:
        file.write(str2)

def get_archive(path):
    with open(path, 'r') as file:
         data = file.read()
    str2= ''
    sub_str = ''
    for char in data:    
        if char.isdigit(): # если все цифры = True
            sub_str += char
        else:
            str2 += char*int(sub_str)
            sub_str = ''
    return str2
    

text = input('Введите текст для архивации: ')

set_archive(text, 'archive.txt')
print(get_archive('archive.txt'))

#Работает правильно при
# архивации одного числа, буквы
# недостатки 
# если идут одинокоый порядок цифр он их не считает
# + зарахивирует неправильно буквы и пробелы

