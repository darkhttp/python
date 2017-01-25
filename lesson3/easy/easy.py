# Задание-1:
# Напишите функцию округлящую полученное произвольное десятичное число,
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные и функции и функции из модуля math


def my_round(number, ndigits):
    number = list(str(number))
    x = ndigits+2
    if int(number[x])>=5:
        del number[x:]
        c = int(number[x-1])+1
        number[x-1]= str(c)
        a = ''.join(number)
        a = float(a)
        return a
    elif x>=9:
        del number[x-1:]
        c = int(number[x])+1
        number[x]= str(c)
        a = ''.join(number)
        a = float(a)

    else:
        del number[x:]
        a = ''.join(number)
        a = float(a)
        return a



a = my_round(2.1234597, 6)
print(a)