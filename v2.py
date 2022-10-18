from zero_level import Square, Rectangle


class Shape:

    def __init__(self, length=0, width=0):
        self.width = width
        self.length = length

    def __str__(self):
        return f' {self.length} - {self.width}'

    def getArea(self):
        if self.width != 0:
            area = self.width * self.length
        else:
            area = self.length * self.length
        return area

    def getPerimeter(self):
        if self.width != 0:
            perimeter = (self.length + self.width) * 2
        else:
            perimeter = 4 * self.length
        return perimeter


class Square(Shape):
    def __init__(self, length):
        super().__init__(length)

    def __str__(self):
        return f'{self.length}'


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def __str__(self):
        return f'{self.length} - {self.width}'


shape1 = Shape(2)
print(shape1)
print(shape1.getArea())
print(shape1.getPerimeter())
rectangle2 = Rectangle(5, 6)
print(rectangle2)
print(rectangle2.getArea())
print(rectangle2.getPerimeter())

from zero_level import Square, Rectangle


class Shape:

    def __init__(self, length=0, width=0): #args
        self.width = width
        self.length = length

    def __str__(self):
        return f' {self.length} - {self.width}'

    def getArea(self):
        if self.width != 0:
            area = self.width * self.length
        else:
            area = self.length * self.length
        return area

    def getPerimeter(self):
        if self.width != 0:
            perimeter = (self.length + self.width) * 2
        else:
            perimeter = 4 * self.length
        return perimeter


class Square(Shape):
    def __init__(self, length): #ok
        super().__init__(length)  #ok

    def __str__(self):
        return f'{self.length}'


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)

    def __str__(self):
        return f'{self.length} - {self.width}'


# shape1 = Shape(2)
# print(shape1)
# print(shape1.getArea())
# print(shape1.getPerimeter())
# rectangle2 = Rectangle(5, 6)
# print(rectangle2)
# print(rectangle2.getArea())
# print(rectangle2.getPerimeter())
# square2 = Square(5)
# print(square2)
# print(square2.getArea())
# print(square2.getPerimeter())

# args
#
# args[0] patrat
# args[0] and args[1] dreptunghi.