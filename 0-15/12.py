
number = int(input('Введите трехзначное число: '))

def DeleteSecondDigit(number):
    return number // 100 * 10 + number % 10

print(DeleteSecondDigit(number))