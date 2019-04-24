
__author__ = 'Белинский Андрей Петрович'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.accuracy = 5

    def perimeter(self):
        ab = math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2)
        ac = math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)
        bc = math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2)
        return round(ab + ac + bc, self.accuracy)

    def square(self):
        # расчет площади по формуле определителя второго порядка
        det = ((self.a[0] - self.c[0]) * (self.b[1] - self.c[1])) - ((self.b[0] - self.c[0]) * (self.a[1]) - self.c[1])
        return round(abs(det)/2, self.accuracy)

    def height(self, point):
        # определение противолежащей стороны
        if point == self.a:
            side = math.sqrt((self.c[0] - self.b[0])**2 + (self.c[1] - self.b[1])**2)
        elif point == self.b:
            side = math.sqrt((self.c[0] - self.a[0])**2 + (self.c[1] - self.a[1])**2)
        elif point == self.c:
            side = math.sqrt((self.b[0] - self.a[0])**2 + (self.b[1] - self.a[1])**2)
        else:
            return f'Точка {point} не является вершиной треугольника'

        s = round(2 * self.square() / side, self.accuracy)
        return f'Высота в треугольнике A{self.a}, B{self.b}, C{self.c} из точки {point} = {s}'


tri1 = Triangle((1, 2), (3, -1), (2, 5))
print(f'Периметр треугольника A{tri1.a}, B{tri1.b}, C{tri1.c} = {tri1.perimeter()}')
print(f'Площадь треугольника A{tri1.a}, B{tri1.b}, C{tri1.c} = {tri1.square()}')
print(tri1.height((2, 5)))
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezium:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def check_isosceles(self):
        ac = math.sqrt((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2)
        bd = math.sqrt((self.d[0] - self.b[0]) ** 2 + (self.d[1] - self.b[1]) ** 2)

        if ac == bd:
            return True
        else:
            return False

    def isosceles(self):
        if self.check_isosceles():
            return 'Трапеция равнобедренная'
        else:
            return 'Трапеция не равнобедренная'

    def lenght(self, p1, p2):
        lenght_pp = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
        return lenght_pp

    def perimeter(self):
        self.ab = self.lenght(self.a, self.b)
        self.bc = self.lenght(self.b, self.c)
        self.cd = self.lenght(self.c, self.d)
        self.ad = self.lenght(self.a, self.d)
        return self.ab + self.bc + self.cd + self.ad

    def square(self):
        if self.check_isosceles():
            if self.ab == self.cd:
                s = (self.bc + self.ad) / 2 * math.sqrt(self.ab**2 - (abs(self.bc - self.ad) / 2)**2)
            else:
                s = (self.ab + self.cd) / 2 * math.sqrt(self.bc ** 2 - (abs(self.ab - self.cd) / 2) ** 2)
            return round(s, 5)
        else:
            return None


trap1 = IsoscelesTrapezium((2, 4), (0, 2), (0, 7), (2, 5))
print(trap1.isosceles())
print('AB =', round(trap1.lenght((2, 4), (0, 2)), 5))
print('P =', round(trap1.perimeter(), 5))
print('S =', trap1.square())
