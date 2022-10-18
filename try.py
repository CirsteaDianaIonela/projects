from math import pi, sqrt
from abc import ABC, abstractmethod


class Corners:
    def __init__(self, number_corners=0, number_90degrees_corners=0):
        self.number_corners = number_corners
        self.number_90degrees_corners = number_90degrees_corners

    def get_no_corners(self):
        return self.number_corners

    def get_number_90degrees_corners(self):
        return self.number_90degrees_corners

    def set_no_corners(self, number_corners):
        self.number_corners = number_corners
        return self.number_corners

    def set_number_90degrees_corners(self, number_90degrees_corners):
        self.number_90degrees_corners = number_90degrees_corners
        return self.number_90degrees_corners

# corner1 = Corners(5, 7)
# print(corner1.get_no_corners())
# print(corner1.set_no_corners(100))
# print(corner1.get_number_90degrees_corners())
# print(corner1.set_number_90degrees_corners(2))


class Shape(ABC, Corners):

    def __init__(self):
        super().__init__()
        self.color = "black"
        pass

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def getPerimeter(self):
        pass

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

class Triangle(Shape, Corners):
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


class ShapeUtils:

    def __init__(self, *shapes: Shape):
        self.list = list(shapes)

    def __str__(self):
        return self.list

    def addShape(self, new_object: Shape):  #adaugam obiecte noul nou creat de tip square/rectangle doar obiecte de tip shape sau care mostenesc shape
        return self.list.append(new_object)

    def getShapesArea(self):
        self.sum = 0
        for item in self.list:
            self.sum += item.getArea()
        return self.sum


    def getShapesPerimeter(self):  #merge cu introducerea culorii, dar vreau sa imi insumeze si daca vreau pentru toate culorile
        self.sum = 0
        for item in self.list:
            self.sum += item.getPerimeter()
        return self.sum

class Color:
    RED = "red" #constanta
    PINK = "pink" #constanta
    @staticmethod
    def get_colouring(new_object: Shape):
        return new_object.color


    @staticmethod
    def set_colouring(new_object: Shape, color):
        new_object.color = color

circle1=Circle(10)
print(circle1.get_no_corners())
print(circle1.get_number_90degrees_corners())
print(circle1.set_no_corners(0))
print(circle1.set_number_90degrees_corners(0))
print(circle1.getPerimeter())
print(circle1.getArea())

triangle1 = Triangle(10, 12, 15)
print(triangle1.number_corners)
print(triangle1.number_90degrees_corners)
print(triangle1.set_no_corners(3))
print(triangle1.set_number_90degrees_corners(1))

utils1 = ShapeUtils(circle1, triangle1)
print(utils1.list)
print(Color.get_colouring(circle1))
Color.set_colouring(circle1, 'red')
print(circle1.color)
Color.set_colouring(triangle1, 'yellow')
print(triangle1.color)

