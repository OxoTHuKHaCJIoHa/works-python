# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import  math


class Treugolnik:
    ab = 100

    ac = 100
    bc = 200
    print("основание треугольника 200")
    print("высота треугольника 50")
    def set(self):
        return  self.ab + self.ac + self.bc
    def get(self):
        return ((self.bc/2)*50)/2


rect1 = Treugolnik()
print(rect1.set())
print(rect1.get())




# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

import math
class one():
     ba = input("Введите длину левой стороны:")
     cd = input("Введите длину правой стороны:")
     ad = input("Введите длину основания:")
     bc = input("Введите длину вершины:")
     print("Трапеция имеет длину сторон:", ba, cd, ad, bc)
     if ba + ad == cd + ad:
         print("Предмет является равнобедренной  трапецией!")
     else:
        print("другая фигура, но нам всё равно, мы продолжаем")
class Chudo:
    def __init__(self, ba, cd, ad, bc):
        super().__init__(ba, cd, ad, bc)
    def set(self):
        return  self.ba + self.ad + self.bc + self.cd
    def get(self):
        return (self.ad + self.bc)/4*math.sqrt(4*(self.ba * self.ba) - (self.ad - self.bc)*(self.ad - self.bc))

print("Периметр и площадь:")
rect1 = one()
print(rect1.set())
print(rect1.get())