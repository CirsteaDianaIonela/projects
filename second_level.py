from first_level import Shape
from third_level import Color

class ShapeUtils(Color):

    def __init__(self, *shapes: Shape):
        super().__init__()
        self.list = list(shapes)

    def __str__(self):
        return self.list

    def addShape(self, new_object: Shape):  #adaugam obiecte noul nou creat de tip square/rectangle doar obiecte de tip shape sau care mostenesc shape
        return self.list.append(new_object)

    def getShapesArea(self, color):
        self.sum = 0
        for item in self.list:
            if color == 'all':
                self.sum += item.getArea()
            elif item.color == color:
                self.sum += item.getArea()
        return self.sum


    def getShapesPerimeter(self, color=None):  #merge cu introducerea culorii, dar vreau sa imi insumeze si daca vreau pentru toate culorile
        self.sum = 0
        for item in self.list:
            if color == None or len(color) == 0:
                self.sum += item.getPerimeter()
            elif item.color == color:
                self.sum += item.getPerimeter()
        return self.sum

#am instantiat 2 obiecte din clasele din first level
# square6 = Square(2)
# rectangle6 = Rectangle(2, 4)
#
# #am instantiat un obiect de clasa ShapeUtils
# utils1 = ShapeUtils(square6, rectangle6)
# print(utils1.list)  #afiseaza lista cu obiectele de tip shape (square and rectangle)
#
# #am calculat si afisat aria si perimetrul obiectelor deja create de tip shape
# print(utils1.getShapesArea())
# print(utils1.getShapesPerimeter())
#
# #am instantiat inca un obiect de tip shape
# rectangle8 = Rectangle(2, 5)
# #adaugam obiectul in lista de shapes
# utils1.addShape(rectangle8)
#
# #am recalculat aria si perimetrul pentru toate obiectele de tip shape folosindu-ne de clasa ShapeUtils
# print(utils1.getShapesArea())
# print(utils1.getShapesPerimeter())
# print(utils1.list)  #afiseaza lista cu obiectele de tip shape (square and rectangle)
# utils1.addShape(list[1, 2])
# print(utils1.getShapesArea())
# utils2 = ShapeUtils(list[1, 2])
# print(utils2.list)
