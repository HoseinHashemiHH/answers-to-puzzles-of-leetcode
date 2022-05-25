

#shortest path problem between two point

from math import sqrt


class Point():
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
p1=Point(19.1,89)
p2=Point(39,9.1)
p3=Point(12.1,-2)
def dist(p1,p2):
    print(p1.x)
    return sqrt((p1.x-p2.x)**2+(p2.y-p1.y)**2)

print(min(dist(p1,p2),dist(p1,p3),dist(p2,p3)))

