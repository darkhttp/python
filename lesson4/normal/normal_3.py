# Задача-3:
# Напишите скрипт заполняющий указанный файл (самомстоятельно задайте имя файла) произвольными целыми
# цифрами, в результате в файле должно быть 2500-значное произвольное число
# Найдите и выведите самую длинную последовательность одинаковых цифр в вышезаполненном файле
#1 вариант
import random
import os
import re
i = 0
a = []
while i<2501:
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
c = [[]]
old = -1

for i in b:
    if int(i) != int(old):
        c.append([])
    old = i
    c[-1].append(i)
print(c)
lmax = max(len(i) for i in c)
print (lmax)
for i in [_ for _ in c if len(_) == lmax]:
    print (i)

#2 вариант
import os
import random
a = [str(random.randint(0,9)) for _ in range(2500)]
b = "".join(a)
print(b)