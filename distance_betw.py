

# distance between two cities with having latitude and longitude


from math import sqrt
class City():
    def __init__(self, lat, long):
        self.lat=lat
        self.long=long
city1=City(100,90)
city2=City(56,24)
dist=sqrt((city1.lat-city2.lat)**2+(city1.long-city2.long)**2)
print('city1 is in {},{} and city2 is in {},{} and the distance betw them is {}'.\
    format(city1.lat,city1.long,city2.lat,city2.long, round(dist,3)))