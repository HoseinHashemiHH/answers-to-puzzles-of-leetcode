

from math import pi


while True:
   try:
    i=int(input("your favourite float numbers of pi is: "))
   except:
    print("please write a digit without percision: ")
    continue
   break
def perc_num(x):
    print('{} is pi with {} percision number'.format(round(pi,x), x))

a=perc_num(i)


