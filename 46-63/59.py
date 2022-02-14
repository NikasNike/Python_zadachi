# 59.	Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
from random import randint



sweets = 200
max_sweets = 28
turn = 1

intellect = int(input('1 = с ителектом, 2 = без интилекта: '))


def clue(sweets, max_sweets):
    if sweets <= max_sweets:
        return sweets
    num = sweets // max_sweets
    num1 = num * max_sweets +1
    if sweets - num1 == 0:
        return 28
    else:
        return sweets - num1

def get_sweets():
    while True:
        if turn ==1 :
            print(f'заберите: {clue(sweets, max_sweets)} конфет')
            sweet_count = int(input(f'Сколько забрать {turn}: '))
        else:
            if intellect == 1:
                sweet_count = clue(sweets, max_sweets) 
            elif intellect == 2:
                sweet_count = randint(1, sweets if max_sweets > sweets else max_sweets)
            print(f'Бот Ввел число: {sweet_count}')
        if sweet_count <= max_sweets:
            return sweet_count
        else: print('!!!!Введите число от 1 до 28!!!!')

while True:
    print(f'Конфет осталось {sweets}')
    sweets -= get_sweets()
    if sweets <= 0:
        turn = 'Бот' if turn == 2 else 'Человек'
        print(f'Победил игрок{turn}')
        break
    turn = 2 if turn == 1 else 1
