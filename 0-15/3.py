#по заданному номеру дня недели вывести его название

#a = int(input('введите число: '))
#
#if (a==1): print ("Понедельник")
#elif (a==2): print ("Вторник")
#elif (a==3): print ("Среда")
#elif (a==4): print ("Четверг")
#elif (a==5): print ("Пятница")
#elif (a==6): print ("Суббота")
#elif (a==7): print ("Воскресенье")
#else:
#    print("Ошибочка вышла")

from ast import Num


def Day (num):
    if num > 7 or num < 1: return False
    kist = ['Понедельник', 'Вторник', 'Среда',
            'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    return kist[num - 1]

print(Day(7))