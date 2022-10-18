from first_level import Shape, Square, Rectangle
from math import pi
from math import sqrt
from fourth_level import Corners

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius


    def getArea(self):
        self.area = (self.radius**2)*pi
        return self.area

    def getPerimeter(self):
        self.perimeter = 2*pi*self.radius
        return self.perimeter


class Trapeze(Shape):
    def __init__(self, base1, base2, l1, l2, h=0):
        super().__init__()
        self.base1 = base1
        self.base2 = base2
        self.h = h
        self.l1 = l1
        self.l2 = l2

    def getArea(self):
        self.area = ((self.base1 + self.base2)*self.h)/2
        return self.area

    def getPerimeter(self):
        self.perimeter = self.base1 + self.base2 + self.l1 + self.l2
        return self.perimeter


class Triangle(Shape):
    def __init__(self, l1, l2, l3):
        super().__init__()
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def getArea(self):
        self.p = (self.l1 + self.l2 + self.l3)/2
        self.area = sqrt(self.p*(self.p-self.l1)*(self.p-self.l2)*(self.p-self.l3))

        return self.area

    def getPerimeter(self):
        self.perimeter = self.l1 + self.l2 + self.l3
        return self.perimeter


class Color:
    RED = "red" #constanta
    PINK = "pink" #constanta
    @staticmethod
    def get_colouring(new_object: Shape):
        return new_object.color


    @staticmethod
    def set_colouring(new_object: Shape, color):
        new_object.color = color


# circle1 = Circle(3)  #instantiez obiectul
# print(circle1)
# print(Color.get_colouring(circle1))  #getter: afisez culoarea obiectului
# Color.set_colouring(circle1, Color.RED)  #setter: setez culoarea obiectului
# print(Color.get_colouring(circle1))  #getter: afisez culoarea obiectului
# print(circle1.getArea())
# print(circle1.getPerimeter())
# print(Corners.get_no_corners(circle1))
# print(circle1.get_no_corners())
# print(circle1.set_no_corners(0))
# print(circle1.get_number_90degrees_corners())
# print(circle1.set_number_90degrees_corners(0))

# square10 = Square(10)
# Color.set_colouring(square10, 'orange')
# print(Color.get_colouring(square10))
# print(square10.getArea())
# print(square10.getPerimeter())

# triangle1 = Triangle(50, 14, 48)
# Color.set_colouring(triangle1, "blue")
# print(Color.get_colouring(triangle1))
# print(triangle1.getPerimeter())
# print(triangle1.getArea())

# trapeze1 = Trapeze(7, 3, 8, 6, 5)
# # print(Corners.get_no_corners(trapeze1))
# print(trapeze1.get_no_corners())
# print(trapeze1.set_no_corners(4))
# print(Corners.get_number_90degrees_corners(trapeze1))
# print(trapeze1.set_number_90degrees_corners(2))
# print(trapeze1.getPerimeter())
# print(trapeze1.getArea())
