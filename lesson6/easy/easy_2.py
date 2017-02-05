# Задача-2: Написать Класс Равнобочная трапеция, заданной координатами 4-х точек.
#  Предусмотреть в классе методы: проверка, является ли фигура равнобочной трапецией;
#  вычисления: длины сторон, периметр, площадь.
import math
class Ravnoboc:
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4

    def proverka(self):
        AB = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        CD = math.sqrt(((self.x3 - self.x4) ** 2) + ((self.y3 - self.y4) ** 2))

        if AB == CD:
           return "Трапеция равнобоковая"
        else:
           return "Трапеция неравнобоковая"


    def storon(self):
        AB = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = self.x3 - self.x2
        CD = math.sqrt(((self.x3 - self.x4) ** 2) + ((self.y3 - self.y4) ** 2))
        AD = self.x4-self.x1
        return AB,BC,CD,AD
    def perimetr(self):

        AB = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = self.x3 - self.x2
        CD = math.sqrt(((self.x3 - self.x4) ** 2) + ((self.y3 - self.y4) ** 2))
        AD = self.x4-self.x1

        per = AB+BC+CD+AD
        return per
    def ploch(self):
        AB = math.sqrt(((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))
        BC = self.x3 - self.x2
        CD = math.sqrt(((self.x3 - self.x4) ** 2) + ((self.y3 - self.y4) ** 2))
        AD = self.x4-self.x1
        if AB == CD:
            s = ((AD + BC) / 2) * (math.sqrt(AB ** 2 - (AD - BC) ** 2 / 4))  # исключительно для равнобоковой трапеции
            return s
        else:
           return "Трапеция неравнобоковая, нельзя вычислить площадь"

        return s
trap = Ravnoboc(1,1,4,7,8,7,11,1)
print(trap.proverka())
print("Cтороны:",trap.storon())
print("Периметр:",trap.perimetr())
print("Площадь:",trap.ploch())





