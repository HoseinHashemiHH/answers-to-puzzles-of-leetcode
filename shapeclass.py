#Shape Area and Perimeter Classes - Create an abstract class called Shape and
#then inherit from it other shapes like diamond, rectangle, circle, triangle etc.
#Then have each class override the area and perimeter functionality to handle
#each shape type.
import math
class Shape():
    def __init__(self,side,vertex) -> None:
        self.side=side
        self.vertex=vertex

class Circle(Shape):
    pi=3.14
    def __init__(self,radius) -> None:
        self.side=0
        self.vertex=0
        self.radius=radius
    def perimeter(self):
        prim1=Circle.pi*2*self.radius
        return prim1
    def area(self):
        area1=Circle.pi*self.radius**2
        return area1
class Squar(Shape):
    def __init__(self, sidesize) -> None:
        self.side=4
        self.vertex=4
        self.sidesize=sidesize
    def area(self):
        area1=self.sidesize*2
        return area1
    def perimeter(self):
        perim1=self.sidesize*4
        return perim1
class Diamond(Shape):
    def __init__(self, small_diagsize,large_diagsize) -> None:
        self.side=4
        self.vertex=4
        self.small_diagsize=small_diagsize
        self.large_diag_size=large_diagsize
    def area(self):
        area1=self.small_diagsize*self.large_diag_size*0.5
        return area1
    def perimeter(self):
        self.sidesize=math.sqrt(self.small_diagsize**2+self.large_diag_size**2)
        prim1=4*self.sidesize
        return prim1

d1=Diamond(19,8.7)
print(d1.area(),d1.perimeter())
        



        