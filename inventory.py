

#Product Inventory Project - Create an application which manages an inventory of
#products. Create a product class which has a price, id, and quantity on hand.
#Then create an inventory class which keeps track of various products and can
# sum up the inventory value.
class Product():
    def __init__(self,price,id,quant) -> None:
        self.price=price
        self.id=id
        self.quant=quant
    def total_price(self):
        return self.price*self.quant

laboo=Product(20,1002,1000)
date=Product(100,1003,600)
lentile=Product(15,1004,800)
inv1=laboo.total_price()
inv2=date.total_price()
inv3=lentile.total_price()
print('laboo is {} and date is {} and lentile is {} totally'.format(inv1,inv2, inv3))
