# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определть методы позволяющие вычислить: Площадь, высоту и периметр фигуры
from math import sqrt
class Treyg:
    import math
    def __init__(self,x1,y1,x2,y2, x3,y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def ploch(self):
        AB = sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = sqrt(((self.x3 - self.x2) ** 2) + ((self.y2 - self.y3) ** 2))
        CD = self.x3-self.x1
        p=(AB+BC+CD)/2
        pl = sqrt(p*((p-AB)*(p-BC)*(p-CD)))
        #p=2
        #s = math.sqrt(p(p-self.a)*(p-self.b)*(p-self.c))
        return pl
    def perimetr(self):
        AB = sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = sqrt(((self.x3 - self.x2) ** 2) + ((self.y2 - self.y3) ** 2))
        CD = self.x3-self.x1
        per=AB+BC+CD
        return per


    def high(self):

        AB = sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = sqrt(((self.x3 - self.x2) ** 2) + ((self.y2 - self.y3) ** 2))
        CD = self.x3-self.x1
        p = (AB + BC + CD) / 2
        pl = sqrt(p * ((p - AB) * (p - BC) * (p - CD)))
        h = (pl*2)/CD
        return h

treygol = Treyg(1,1,3,5,8,1)

print("Площадь:",treygol.ploch())
print("Периметр:",treygol.perimetr())
print("Высота:",treygol.high())

