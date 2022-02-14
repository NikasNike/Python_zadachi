#Написать программу вычисления произведения чисел от 1 до N
def mess(N):
    sum = 1
    for i in range(1, N+1):
        sum = i * sum
        print(sum)
mess(5)


