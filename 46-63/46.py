#Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов
def fiboanchi(n):
    if n in [0, 1] : return 1
    if n > 0: return fiboanchi(n-1) + fiboanchi(n - 2)
    if n < 0: return fiboanchi(n+2) - fiboanchi(n+1)

def list(s_N, e_N):
    num_fib = []
    for i in range(s_N, e_N):
        num_fib.append(fiboanchi(i))
    return num_fib

s_N = int(input('Начало: '))
e_N = int(input('Конец: '))
lst_fibo = list(s_N, e_N)
print(lst_fibo)

