
class tile():
    def __init__(self,height,width):
        self.height=height
        self.width=width
        self.area=self.height*self.width
    def cost(self):
        cst=self.area*1000
        return cst
tile1=tile(12,13)
print(type(tile1))
tile_c=tile1.cost()
print(tile_c)