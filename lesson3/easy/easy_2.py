# Задание-2:
# Дан шестизначный номер билета, определить является ли билет счасливым
# Решение реализовать в виде функции
# Билет считается счастливым, если сумма его первых и последних цифр равны
# !!!P.S.: функция не должна НИЧЕГО print'ить

#1-й вариант
def lucky_ticket(a,b,c,d,e,f):
    if a+b+c==d+e+f:
        return True
    else:
        return False


c = lucky_ticket(1,1,1,1,1,1)
if c == True:
    print('Счастливый билет')
else:
    print('Несчастливый билет')

print('-'*100)
#2-й вариант
def lucky_ticket(c):
    result=0
    result1=0
    for i in c[:3]:
        result+=int(i)
    for i in c[3:]:
        result1+=int(i)
    if result==result1:
        return True
    else:
        return False
c = list(str(input("Номер билета")))
d = lucky_ticket(c)
if d == True:
    print('Счастливый билет')
else:
    print('Несчастливый билет')
