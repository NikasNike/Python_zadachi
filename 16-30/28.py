#Подсчитать сумму цифр в числе
def SumNum(num):
    num1 = str(num)
    rev = 0
    for i in num1:
        rev += int(i)
    print(rev)
SumNum(12345)  
