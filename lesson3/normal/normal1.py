# Задание-1:
# Напишите функцию возвращающую ряд Фибоначчи с n-элемента до m-элемент
# Первыми элементами ряда считать цифры 1 1
def fib(n, m):
    prev = 0
    next = 0
    while next < m:
        next = n + prev
        n = prev
        prev = next
        print(next)

fib(1, 144)
