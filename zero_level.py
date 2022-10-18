class Square:

    @staticmethod
    def calculateArea(length):
        area = length*length
        return area

    @staticmethod
    def calculatePerimeter(length):
        perimeter = length*4
        return perimeter


class Rectangle:

    @staticmethod
    def calculateArea(length, width):
        area = length * width
        return area

    @staticmethod
    def calculatePerimeter(length, width):
        perimeter = 2*(length + width)
        return perimeter


# print(Square.calculateArea(2))
# print(Square.calculatePerimeter(2))
# print(Rectangle.calculateArea(2, 5))
# print(Rectangle.calculatePerimeter(2, 5))
