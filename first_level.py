from abc import ABC, abstractmethod
from fourth_level import Corners

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


class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def getArea(self):
        self.area = self.length**2
        return self.area

    def getPerimeter(self):
        self.perimeter = self.length*4
        return self.perimeter


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def getArea(self):
        self.area = self.length * self.width
        return self.area

    def getPerimeter(self):
        self.perimeter = 2*(self.length + self.width)
        return self.perimeter


# square5 = Square(2)
# print(square5.getArea())
# print(square5.getPerimeter())
# rectangle5 = Rectangle(2, 3)
# print(rectangle5.getArea())
# print(rectangle5.getPerimeter())
