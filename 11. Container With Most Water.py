
from collections import defaultdict

from numpy import iterable
def c_area(ar):
    s=defaultdict(list)
    t=reversed(ar)
    for x,a in enumerate(ar):
        for y,b in enumerate(ar):
            s[(y-x)*min(b,a)].append((x,y))
            print(s)
    for k,v in s.items():
        if k==max(s.keys()):
            return k,v
    
c,y=c_area([1,8,6,2,5,4,8,3,7])

print(c,'-->',y[0])

c,y=c_area([1,1])

print(c,'-->',y[0])



