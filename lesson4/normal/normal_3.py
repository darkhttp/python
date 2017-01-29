# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле
import random
import os
import re
i = 0
a = []
while i<50:
    lst_g = random.randint(0,9)
    i+=1
    a.append(str(lst_g))

l=''.join(a)
file = open('test.txt','w')
file.write(l)
file.close
file = open('test.txt','r')
b = file.read()
print(b)

i = 0
c = 0

for i in list(b):
    if i==i:
        c+=1
        max = i
        print(i)
        if int(i)>c:
            maxlen = c
            print(c)


