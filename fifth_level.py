from first_level import Square, Rectangle
from second_level import ShapeUtils
from third_level import Circle, Triangle, Trapeze, Color

#instantiez obiectele
square_first = Square(2)
square_first.set_no_corners(4)
rectangle_first = Rectangle(2, 3)
rectangle_first.set_no_corners(4)
circle_first = Circle(2)
circle_first.set_no_corners(0)
triangle_first = Triangle(2, 3, 4)
triangle_first.set_no_corners(3)
trapeze_first = Trapeze(2, 3, 4, 5, 6)
trapeze_first.set_no_corners(4)
#adaug obiectele in lista
utils_first = ShapeUtils(square_first, rectangle_first, circle_first, triangle_first, trapeze_first)

# lista = []
#iterez prin lista si setez culoarea in functie de nr de colturi

for item in utils_first.list:
    if item.number_corners == 4:
        item.set_colouring("red")
    else:
        item.set_colouring("yellow")

#spun culoarea pentru care vreau sa calculez suma perimeterelor
start_color = input("Tell me the color: ")
print(utils_first.getShapesPerimeter(start_color)) #calculez perimetrul pentru o culoare specifica
# print(utils_first.getShapesArea(start_color)) #calculez perimetrul pentru o culoare specifica



#rezulatul dorit este = perimetru triangle 9 + circle 12.56 = 21.56




