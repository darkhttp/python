# Задание-1:
# Написать программу выполняющую операции(сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 2/3
def func(a):
    b=[]
    c=[]
    n = 0

    for i in a:
        for i in i:
            b.append(i)

    if b[3]=='+':
        l = int(b[0])*int(b[6])
        d = int(b[2])*int(b[6])
        f = int(b[4])*int(b[2])
        e = int(b[6])*int(b[2])
        g = l+f
        while g>d:

            o = g-d
            n+=1
            g=o
        print(n,'{}/{}'.format(g,d))
    if b[3]=='-':
        l = int(b[0])*int(b[6])
        d = int(b[2])*int(b[6])
        f = int(b[4])*int(b[2])
        e = int(b[6])*int(b[2])
        g = l-f
        while g>d:

            o = g-d
            n-=1
            g=o
        if n>0:
            print(n,'{}/{}'.format(g,d))
        if n < 0:
            print(n, '{}/{}'.format(g, d))
        else:
            print('{}/{}'.format(g, d))
i = input(":")
a=i.split()
func(a)

