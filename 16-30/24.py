 #Найти кубы чисел от 1 до N

n = int(input('N = '))
li = [x for x in range(1, n+1)]
li = list(map(lambda x:x+10, li))
print(li)
