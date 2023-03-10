import math

class Circle:
    def init__(self, radius):
        self.__radius = radius

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def _add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)

c1= Circle(4)
print(c1.getRadius())
c2 = Circle(5)

print(c2.getRadius())
c3 =c1 + c2 

print(c3.getRadius())