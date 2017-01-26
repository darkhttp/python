# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма
#x1=x2 x3=x4 y2=y3 y1=y4

a1=1,4
a2=1,5
a3=4,5
a4=4,4
def parl(*args):
    x=[]
    y=[]

    for i in args:
        x.append(i[0])
        y.append(i[1])
    if x[0]==x[1] and x[2]==x[3]:
        if  y[1]==y[2] and y[0]==y[3]:
            return True
        else:
            return False
    else:
        return False

c = parl(a1,a2,a3,a4)
if c == True:
    print('Это параллелограмм')
else:
    print('Это не параллелограмм')